"""PROJ_4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from PROJ_4_APP.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_template, name='base_template'),
    path('singleproduct/<slug:slug>', singleproduct.as_view(), name='shopitem'),
    path('allproducts', all_products, name='allproducts'),
    path('about', about, name='about'),
    path('posters', posters, name='posters'),
    path('canvas', canvas, name='canvas'),
    path('frames', frames, name='frames'),
    path('accounts/', include('allauth.urls')),
    path('my_account', my_account, name='my_account'),
    path('view_orders', view_orders, name='view_orders'),
    path('change_userinfo', change_userinfo, name='change_userinfo'),
    path('return_order', return_order, name='return_order'),
    path('custom_request', custom_request, name='custom_request'),
    path('contact_support', contact_support, name='contact_support'),
    path('cart', cart, name='cart'),
    path('addtocart', addtocart, name='addtocart'),
    path('update-cart', updatecart, name='update-cart'),
    path('delete-cart-item', deletecartitem, name='delete-cart-item'),
]
