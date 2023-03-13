# Generated by Django 4.1.7 on 2023-03-13 10:28

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_singleproduct_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('first_name', models.CharField(max_length=40, unique=True)),
                ('last_name', models.CharField(max_length=40, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]
