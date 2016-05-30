from django.test import TestCase

from store.factories import BrandFactory, SparePartFactory


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

    def test_can_filter_by_spare_part_name(self):
        spare_part1 = SparePartFactory()
        spare_part2 = SparePartFactory()

        response = self.client.get('/store/?q=%s' % '+'.join(spare_part1.name.split()))
        self.assertEqual(list(response.context['spare_parts']), [spare_part1])

        response = self.client.get('/store/?q=%s' % '+'.join(spare_part2.name.split()))
        self.assertEqual(list(response.context['spare_parts']), [spare_part2])

    def test_can_filter_by_brand_name(self):
        brand1 = BrandFactory()
        brand2 = BrandFactory()
        spare_part1 = SparePartFactory(brand=brand1)
        spare_part2 = SparePartFactory(brand=brand2)

        response = self.client.get('/store/?q=%s' % '+'.join(brand1.name.split()))
        self.assertEqual(list(response.context['spare_parts']), [spare_part1])

        response = self.client.get('/store/?q=%s' % '+'.join(brand2.name.split()))
        self.assertEqual(list(response.context['spare_parts']), [spare_part2])


class SparePartDetailTest(TestCase):

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


class StatisticsTest(TestCase):

    def setUp(self):
        self.brand1 = BrandFactory()
        self.brand2 = BrandFactory()
        self.brand3 = BrandFactory()

        for _ in range(5):
            SparePartFactory(brand=self.brand1)
            SparePartFactory(brand=self.brand2)

        SparePartFactory(brand=self.brand1)

        self.response = self.client.get('/store/stats/')

    def test_renders_correct_result(self):
        self.assertTemplateUsed(self.response, 'store/stats.html')

    def test_shows_only_brands_with_5_or_more_spare_parts(self):
        self.assertNotContains(self.response, self.brand3.name)

    def test_brands_sorted_by_number_of_spare_parts(self):
        self.assertEqual(list(self.response.context['brands']), [self.brand1, self.brand2])
