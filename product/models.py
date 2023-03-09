from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Categorie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
    class Meta:
        ordering = ['name',]
        
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Categorie, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    
    class Meta:
        ordering = ['-created_at', '-price', 'price',]
        
    def __str__(self):
        return self.name
