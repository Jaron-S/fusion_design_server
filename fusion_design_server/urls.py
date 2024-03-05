"""
URL configuration for fusion_design_server project.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ecommerce_server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.product_list, name='product_list'),
    path('categories/', views.category_list, name='category_list'),
    path('carousel/', views.carousel_list, name='carousel_list'),
    path('api/products/', views.ProductList.as_view(), name='api_products'),
    path('api/categories/', views.CategoryList.as_view(), name='api_categories'),
    path('api/carousel-items/', views.CarouselItemList.as_view(), name='api_carousel_items'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
