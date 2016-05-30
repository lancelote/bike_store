from django.test import TestCase

from factories import SparePartFactory


class SparePartListTest(TestCase):

    def test_renders_correct_template(self):
        response = self.client.get('/store/')
        self.assertTemplateUsed(response, 'store/list.html')

    def test_shows_warning_if_no_spare_parts_available(self):
        response = self.client.get('/store/')
        self.assertContains(response, 'No spare parts available')

    def test_returns_10_parts_by_page(self):
        spare_parts = [SparePartFactory() for _ in range(11)]
        response = self.client.get('/store/')
        self.assertEqual(list(response.context['spare_parts']), spare_parts[:10])

    def test_second_page_returns_correct_spare_parts(self):
        spare_parts = [SparePartFactory() for _ in range(21)]
        response = self.client.get('/store/?page=2')
        self.assertEqual(list(response.context['spare_parts']), spare_parts[10:20])

    def test_returns_last_page_if_page_is_out_of_range(self):
        spare_parts = [SparePartFactory() for _ in range(11)]
        response = self.client.get('/store/?page=999')
        self.assertEqual(list(response.context['spare_parts']), [spare_parts[10]])


class SparePartDetail(TestCase):

    def setUp(self):
        self.spare_part = SparePartFactory()
        self.response = self.client.get('/store/%d/' % self.spare_part.id)

    def test_renders_correct_template(self):
        self.assertTemplateUsed(self.response, 'store/detail.html')

    def test_response_contains_spare_part_name(self):
        self.assertContains(self.response, self.spare_part.name)

    def test_unknown_spare_part_returns_404(self):
        response = self.client.get('/store/999/')
        self.assertEqual(response.status_code, 404)
