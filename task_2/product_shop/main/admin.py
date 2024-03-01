from django.contrib import admin
from main.models import Category, SubCategory, Product


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
    search_fields = ('category', 'name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory', 'name', 'slug', 'price')
    list_filter = ('subcategory', 'name', 'price',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}