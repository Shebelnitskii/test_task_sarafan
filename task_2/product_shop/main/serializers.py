from rest_framework import serializers
import config.settings
from main.models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='subcategory.category.name')
    subcategory = serializers.StringRelatedField(source='subcategory.name')

    class Meta:
        model = Product
        fields = ['name', 'slug', 'category', 'subcategory', 'price', 'image']
