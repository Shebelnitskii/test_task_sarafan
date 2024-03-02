from django.contrib import admin
from main.models import Category, SubCategory, Product, ShoppingCart, ShoppingCartItem


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'slug')
    list_filter = ('category', 'name',)
    search_fields = ('subcategory', 'name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory', 'name', 'slug', 'price')
    list_filter = ('subcategory', 'name', 'price',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_products')
    list_filter = ('user', )
    search_fields = ('user', )

    def get_products(self, obj):
        return ", ".join([str(product) for product in obj.products.all()])

    get_products.short_description = 'Products'

@admin.register(ShoppingCartItem)
class ShoppingCartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity')
    list_filter = ('product',)  # Замените 'product' на ('product',)
    search_fields = ('product',)  # Замените 'product' на ('product',)