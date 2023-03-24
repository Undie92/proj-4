from django.test import TestCase
from .models import *

class TestModels(TestCase):

    def test_get_category(self):
        category = Category.objects.create(name='test name', slug='test-name')
        self.assertTrue(category.name=='test name')
        self.assertTrue(category.slug=='test-name')

    def test_get_products(self):
        product = Category.objects.create(name='test name', slug='test-name')
        self.assertTrue(product.name=='test name')
        self.assertTrue(product.slug=='test-name')

    def test_get_singleproduct(self):
        singleproduct = Category.objects.create(name='test name', slug='test-name')
        self.assertTrue(singleproduct.name=='test name')
        self.assertTrue(singleproduct.slug=='test-name')

    def test_get_about(self):
        about = About.objects.create(first_name='first test', last_name='last test', slug='slug-slug', city='city', birth_date='1992-03-20')
        self.assertTrue(about.first_name=='first test')
        self.assertTrue(about.last_name=='last test')
        self.assertTrue(about.slug=='slug-slug')
        self.assertTrue(about.city=='city')
        self.assertTrue(about.birth_date=='1992-03-20')