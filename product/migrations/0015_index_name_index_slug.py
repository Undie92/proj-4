# Generated by Django 4.1.7 on 2023-03-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='index',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]