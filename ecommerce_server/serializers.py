from rest_framework import serializers
from .models import Product, Category, CarouselItem

class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'image', 'rating', 'category', 'subCategories', 'colors', 'availability', 'tags']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['imageUrl'] = instance.image.url if instance.image else None
        representation.pop('image', None)
        return representation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'url', 'subCategories']


class CarouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        fields = ['id', 'url', 'image']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['imageUrl'] = instance.image.url if instance.image else None
        representation.pop('image', None)
        return representation
