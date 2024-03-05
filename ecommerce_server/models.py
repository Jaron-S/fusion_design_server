from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/products/', default='null')
    rating = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    subCategories = models.JSONField()
    colors = models.JSONField()
    availability = models.BooleanField()
    tags = models.JSONField()

class Category(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/categories/', default='null')
    url = models.CharField(max_length=255)
    subCategories = models.JSONField()

class CarouselItem(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    url = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/carousel/', default='null')