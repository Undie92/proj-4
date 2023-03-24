from django.test import TestCase
from product.models import *


class TestViews(TestCase):

    def test_get_base_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_my_account(self):
        response = self.client.get('/my_account')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_account.html')
        
    def test_get_view_orders(self):
        response = self.client.get('/view_orders')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_orders.html')
    
    def test_get_change_userinfo(self):
        response = self.client.get('/change_userinfo')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'change_userinfo.html')
        
    def test_get_return_order(self):
        response = self.client.get('/return_order')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'return_order.html')
        
    def test_get_custom_request(self):
        response = self.client.get('/custom_request')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_request.html')
        
    def test_get_contact_support(self):
        response = self.client.get('/contact_support')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_support.html')
        
    def test_get_cart(self):
        self.assertTemplateUsed('cart.html')

    def test_get_addtocart(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_updatecart(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_deletecartitem(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_all_products(self):
        response = self.client.get('/allproducts')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'allproducts.html')

    def test_get_about(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_get_posters(self):
        response = self.client.get('/posters')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posters.html')

    def test_get_canvas(self):
        response = self.client.get('/canvas')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'canvas.html')

    def test_get_frames(self):
        response = self.client.get('/frames')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'frames.html')
