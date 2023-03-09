# Generated by Django 4.1.7 on 2023-03-09 19:24

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_category_categorie_rename_products_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorie',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at', '-price', 'price']},
        ),
        migrations.AddField(
            model_name='product',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
