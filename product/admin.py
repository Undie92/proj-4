from django.contrib import admin
from .models import Category, Product, About, Index


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name', 'slug')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name', 'slug', 'created_at', 'price', 'category')
    search_fields = ['name', 'price']
    list_display = ('name', 'slug', 'created_at', 'price', 'category')
    
admin.site.register(About)

admin.site.register(Index)
