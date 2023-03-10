from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from datetime import datetime
from product.models import Product, Category
# Canvases


def base_template(request):
    return render(request, 'index.html')


def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    active_category = request.GET.get('category', '')
    
    if active_category:
        products = products.filter(category__slug=active_category)
        paginator = Paginator(products, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    
    context = {
        'categories': categories,
        'page_obj': page_obj,
        'active_category': active_category
    }
    
    return render(request, 'allproducts.html', context)



def about(request):
    return render(request, 'about.html')

def posters(request):
    products = Product.objects.all().filter(category__slug="posters")
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    return render(request, 'posters.html', {'page_obj': page_obj})

def canvas(request):

    products_canvas = Product.objects.all().filter(category__slug="canvases")
    paginator = Paginator(products_canvas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    return render(request, 'canvas.html', {'page_obj': page_obj})

def frames(request):
    products_frames = Product.objects.all().filter(category__slug="frames")
    paginator = Paginator(products_frames, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'frames.html', {'page_obj': page_obj})


def shop_item(request):
    return render(request, 'shopitem.html')
    