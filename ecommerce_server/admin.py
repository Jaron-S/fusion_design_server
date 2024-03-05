from django.contrib import admin
from .models import Product, Category, CarouselItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'availability']
    list_filter = ['category', 'availability']
    search_fields = ['title', 'description', 'tags']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    search_fields = ['name']

@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'url']
