from django.shortcuts import render


def base_template(request):
    return render(request, 'index.html')


def shop_item(request):
    return render(request, 'shopitem.html')