from django.shortcuts import render
from .models import Product, Category, CarouselItem
from rest_framework import generics
from .serializers import ProductSerializer, CategorySerializer, CarouselItemSerializer

# View for Products
def product_list(request):
    products = Product.objects.all()  # Retrieve all products from the database
    return render(request, 'product_list.html', {'products': products})

# View for Categories
def category_list(request):
    categories = Category.objects.all()  # Retrieve all categories
    return render(request, 'category_list.html', {'categories': categories})

# View for Carousel Items
def carousel_list(request):
    carousel_items = CarouselItem.objects.all()  # Retrieve all carousel items
    return render(request, 'carousel_list.html', {'carousel_items': carousel_items})

# APIs
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CarouselItemList(generics.ListAPIView):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer