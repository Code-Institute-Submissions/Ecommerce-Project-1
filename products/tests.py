from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import all_products, all_categories, products_by_category, products_detail, product_home
from .models import Product, Category
import json


# Create your tests here.
class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')


class Test_urls(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product Urls
    """
    def test_product_url_is_resolved(self):
        url = reverse('products')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_products)

    def test_product_home_url_is_resolved(self):
        url = reverse('product_home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_home)

    def test_all_categories_url_is_resolved(self):
        url = reverse('category')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_categories)

    def test_products_detail_is_resolved(self):
        url = reverse('products_detail', args=['some_slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, products_detail)

    def test_products_by_category_is_resolved(self):
        url = reverse('products_by_category' , args=['some_slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, products_by_category)


class Test_views(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product views
    """
    def setUp(self):
        self.client = Client()
        self.products_url = reverse('products')
        self.product_home_url = reverse('product_home')
        self.product_detail_url = reverse('products_detail', args=['product1'])
        self.product1 = Product.objects.create(
            name='products1',
            slug='product1',
            price='10'
        )

    def test_all_products_GET(self):
        response = self.client.get(self.products_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html', 'base.html')

    def test_product_home_GET(self):
        response = self.client.get(self.product_home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_home.html', 'base.html')

    def test_products_detail_GET(self):
        response = self.client.get(self.product_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products_detail.html', 'base.html')
