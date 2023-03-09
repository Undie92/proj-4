from django.shortcuts import render
from datetime import datetime


def base_template(request):
    return render(request, 'index.html')


def all_products(request):
    return render(request, 'allproducts.html')


def shop_item(request):
    return render(request, 'shopitem.html')

def about(request):
    return render(request, 'about.html')
