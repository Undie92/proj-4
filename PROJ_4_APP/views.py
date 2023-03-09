from django.shortcuts import render
from django.core.paginator import Paginator
from datetime import datetime
from product.models import Product, Categorie


def base_template(request):
    return render(request, 'index.html')


def all_products(request):
    categories = Categorie.objects.all()
    products = Product.objects.all()
    
    context = {
        'categories': categories,
        'products': products
    }
    
    return render(request, 'allproducts.html', context)



def shop_item(request):
    return render(request, 'shopitem.html')

def about(request):
    return render(request, 'about.html')

def posters(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    return render(request, 'posters.html', {'page_obj': page_obj})