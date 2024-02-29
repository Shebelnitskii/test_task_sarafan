from rest_framework import generics, status
from rest_framework.response import Response
from .models import Category,SubCategory, Product
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer
from .pagination import CategoryPagination, SubCategoryPagination


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination

class SubCategoryListView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = SubCategoryPagination

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # pagination_class =
