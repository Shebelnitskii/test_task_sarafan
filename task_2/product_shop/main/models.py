from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(unique=True, verbose_name='Уникальный идентификатор')
    image = models.ImageField(upload_to='category_images/', **NULLABLE, verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Название подкатегории')
    slug = models.SlugField(unique=True, verbose_name='Уникальный идентификатор')
    image = models.ImageField(upload_to='subcategory_images/', **NULLABLE, verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', verbose_name='Подкатегория')
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    slug = models.SlugField(unique=True, verbose_name='Уникальный идентификатор')
    image = models.ImageField(upload_to='product_images/', **NULLABLE, verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Покупатель')
    products = models.ManyToManyField(Product, through='ShoppingCartItem', related_name='shopping_carts', verbose_name='Продукты в корзине')

    def __str__(self):
        return f"Корзина заказов {self.user}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='items', verbose_name='Корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.IntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"{self.product.name}: {self.quantity} шт."

    class Meta:
        verbose_name = 'Товар корзины'
        verbose_name_plural = 'Товары корзины'