from rest_framework import status
from rest_framework.test import APITestCase

from store.models import SparePart
from store.factories import BrandFactory, SparePartFactory


class SparePartTests(APITestCase):

    def test_create_spare_part(self):
        brand = BrandFactory()

        url = '/api/create/'
        data = {
            'name': 'Test Spate Part',
            'brand': brand.id,
            'price': '123',
            'contact': 'Test Contact'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SparePart.objects.count(), 1)
        self.assertEqual(SparePart.objects.get().name, 'Test Spate Part')

    def test_get_spare_part_list(self):
        url = '/api/list/'
        for _ in range(11):
            SparePartFactory()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 11)  # Total spare parts
        self.assertTrue(response.data['next'].endswith('?page=2'))  # Pagination online
        self.assertEqual(len(response.data['results']), 10)  # Limit number os items per page

    def test_can_search_by_spare_part_name(self):
        url = '/api/list/?search=%s'
        spare_parts = [SparePartFactory() for _ in range(11)]

        search = '+'.join(spare_parts[3].name.split())
        response = self.client.get(url % search)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], spare_parts[3].name)

    def test_can_search_by_brand_name(self):
        url = '/api/list/?search=%s'
        spare_parts = [SparePartFactory() for _ in range(11)]

        search = '+'.join(spare_parts[3].brand.name.split())
        response = self.client.get(url % search)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['brand']['name'], spare_parts[3].brand.name)


class BrandTests(APITestCase):

    def test_can_get_top_brands_stats(self):
        brand1 = BrandFactory()
        brand2 = BrandFactory()
        BrandFactory()  # Brand with less than 5 items

        for _ in range(5):
            SparePartFactory(brand=brand1)
            SparePartFactory(brand=brand2)
        SparePartFactory(brand=brand1)

        url = '/api/stats/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual([response.data[0]['name'], response.data[1]['name']], [brand1.name, brand2.name])
