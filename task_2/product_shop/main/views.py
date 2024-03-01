from rest_framework import generics, status
from rest_framework.response import Response
from .models import Category, SubCategory, Product, ShoppingCart
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer, ShoppingCartSerializer, \
    AddToShoppingCartSerializer
from .pagination import CategoryPagination, SubCategoryPagination, ProductPagination
from rest_framework.permissions import IsAuthenticated


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


class AddToShoppingCartView(generics.CreateAPIView):
    '''Добавление товаров в корзину по id товара'''
    queryset = ShoppingCart.objects.all()
    serializer_class = AddToShoppingCartSerializer


class UpdateShoppingCartItemView(generics.UpdateAPIView):
    '''Обновление кол-ва товара в корзине по id товара в корзине'''
    queryset = ShoppingCart.objects.all()
    serializer_class = AddToShoppingCartSerializer
    lookup_url_kwarg = 'pk'

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class RemoveFromShoppingCartView(generics.DestroyAPIView):
    '''Удаление товара в корзине по id товара в корзине'''
    queryset = ShoppingCart.objects.all()
    lookup_url_kwarg = 'pk'


class ViewShoppingCart(generics.ListAPIView):
    '''Просмотр корзины пользователя'''
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

    def get_queryset(self):
        '''Вывод информации о корзине того пользователя, который сделал запрос'''
        user = self.request.user
        # Фильтруем корзину по пользователю
        queryset = ShoppingCart.objects.filter(user=user)
        return queryset

    def list(self, request, *args, **kwargs):
        '''Подсчёт суммы корзины и кол-ва товаров'''
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        total_items = sum(item.quantity for item in queryset)
        total_cost = sum(item.product.price * item.quantity for item in queryset)
        response_data = {
            'cart_items': serializer.data,
            'total_items': total_items,
            'total_cost': total_cost
        }
        return Response(response_data)


class ClearShoppingCartView(generics.DestroyAPIView):
    '''Очистка корзины пользователя'''
    queryset = ShoppingCart.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        queryset = self.get_queryset().filter(user=user)
        queryset.delete()
        return self.destroy(request, *args, **kwargs)
