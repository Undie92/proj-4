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
from django.urls import path
from PROJ_4_APP.views import base_template, all_products, about, posters, canvas, frames, singleproduct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_template, name='base_template'),
    path('singleproduct/<slug:slug>', singleproduct.as_view(), name='shopitem'),
    path('allproducts', all_products, name='allproducts'),
    path('about', about, name='about'),
    path('posters', posters, name='posters'),
    path('canvas', canvas, name='canvas'),
    path('frames', frames, name='frames')
]
