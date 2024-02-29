# urls.py

from django.urls import path
from .views import CategoryListView,SubCategoryListView, ProductListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('subcategories/', SubCategoryListView.as_view(), name='subcategory_list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    # path('cart/', CartView.as_view(), name='cart'),
]