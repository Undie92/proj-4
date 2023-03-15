from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.views import generic, View
from datetime import datetime
from product.models import *


def base_template(request):
    index = Index.objects.all()
    return render(request, 'index.html', {'index': index})

def my_account(request):
    return render(request, 'my_account.html')

def view_orders(request):
    return render(request, 'view_orders.html')

def change_userinfo(request):
    return render(request, 'change_userinfo.html')

def return_order(request):
    return render(request, 'return_order.html')

def custom_request(request):
    return render(request, 'custom_request.html')

def contact_support(request):
    return render(request, 'contact_support.html')

def cart(request):
    cart = Cart.objects.filter(user=request.user)
    for item in cart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.price * item.product_qty
        
        
    context = {
        'cart': cart,
        'cartitems': cartitems,
        'total_price': total_price,
    }
    
    return render(request, 'cart.html', context)

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status': "Product already in cart."})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >= prod_qty :
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': "Product added successfully"})
                    else:
                        return JsonResponse({'status': "Only "+ str(product_check.quantity) +" quantity available"})
            else:
                return JsonResponse({'status': "No such product found"})
        else:
            return JsonResponse({'status': "Login to Continue"})
        
    return redirect('/')

def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status': "Updated Successfully"})
    return redirect('/')

def deletecartitem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
            cartitem.delete()
            return JsonResponse({'status': "Deleted Successfully"})
    return redirect('/')

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
        'active_category': active_category,
    }
    
    return render(request, 'allproducts.html', context)



def about(request):
    about = About.objects.all()
    context = {
        'about': about
    }
    return render(request, 'about.html', context)

def posters(request):
    products = Product.objects.all().filter(category__slug="posters")
    paginator = Paginator(products, 8)
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



class singleproduct(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Product.objects.filter()
        product = get_object_or_404(queryset, slug=slug)
        
        return render(
            request,
            "shopitem.html",
            {'product': product}
        )
