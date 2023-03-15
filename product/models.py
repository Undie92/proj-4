from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
    class Meta:
        ordering = ['name',]
        
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    quantity = models.IntegerField(null=True, blank=True)


    class Meta:
        ordering = ['created_at', '-price', 'price',]
        
    def __str__(self):
        return self.name
    
class SingleProduct(models.Model):
    category = models.ForeignKey(Category, related_name='singleproduct', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class About(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    first_name = models.CharField(max_length=40, unique=True)
    last_name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    birth_date = models.DateField()
    interests = models.CharField(max_length=255, blank=True, null=True)
    speciality = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    
        
    def __str__(self):
        return self.first_name
    
    
    def get_age(self):
        age = datetime.date.today()-self.birth_date
        return int((age).days/365.25)
    
class Index(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    name = models.CharField(max_length=255, unique=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
