# urls.py

from django.urls import path
from .views import CategoryListView, SubCategoryListView, ProductListView, AddToShoppingCartView, \
    UpdateShoppingCartItemView, RemoveFromShoppingCartView, ViewShoppingCart, ClearShoppingCartView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('subcategories/', SubCategoryListView.as_view(), name='subcategory_list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('shopping_cart/add/', AddToShoppingCartView.as_view(), name='add'),
    path('shopping_cart/update/<int:pk>/', UpdateShoppingCartItemView.as_view(), name='update'),
    path('shopping_cart/delete/<int:pk>/', RemoveFromShoppingCartView.as_view(), name='delete'),
    path('shopping_cart/list/', ViewShoppingCart.as_view(), name='list'),
    path('shopping_cart/clear/', ClearShoppingCartView.as_view(), name='clear'),
]
