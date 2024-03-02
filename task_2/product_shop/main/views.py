from rest_framework import generics, status
from rest_framework.response import Response
from main.models import Category, SubCategory, Product, ShoppingCart, ShoppingCartItem
from main.serializers import CategorySerializer, SubCategorySerializer, ProductSerializer, ShoppingCartSerializer, \
    AddToShoppingCartSerializer, UpdateShoppingCartItemSerializer
from main.pagination import CategoryPagination, SubCategoryPagination, ProductPagination
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class CategoryListView(generics.ListAPIView):
    '''Просмотр списка категорий'''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination


class SubCategoryListView(generics.ListAPIView):
    '''Просмотр списка подкатегорий'''
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = SubCategoryPagination


class ProductListView(generics.ListAPIView):
    '''Просмотр списка продуктов'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination


class ViewShoppingCart(generics.ListAPIView):
    '''Просмотр корзины пользователя'''
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class AddToShoppingCartView(generics.CreateAPIView):
    '''Добавление товаров в корзину по id товара'''
    queryset = ShoppingCartItem.objects.all()
    serializer_class = AddToShoppingCartSerializer


class UpdateShoppingCartItemView(generics.UpdateAPIView):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = UpdateShoppingCartItemSerializer
    lookup_url_kwarg = 'pk'

    def perform_update(self, serializer):
        '''Выполнение обновления'''
        instance = serializer.save()
        if instance.quantity < 0:
            raise ValidationError("Количество товара не может быть отрицательным.")


class RemoveFromShoppingCartView(generics.DestroyAPIView):
    '''Удаление товара в корзине по id товара в корзине'''
    queryset = ShoppingCartItem.objects.all()
    lookup_url_kwarg = 'pk'


class ClearShoppingCartView(generics.DestroyAPIView):
    '''Очистка корзины пользователя'''
    queryset = ShoppingCartItem.objects.all()
    permission_classes = [IsAuthenticated]


    def delete(self, request, *args, **kwargs):
        '''Очистка корзины польщователя, который отправил запрос'''
        queryset = self.get_queryset()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
