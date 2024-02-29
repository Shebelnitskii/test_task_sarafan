from rest_framework import serializers
import config.settings
from main.models import Category, SubCategory, Product, ShoppingCart


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


class ShoppingCartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ShoppingCart
        fields = ['id', 'user', 'product', 'quantity']


class AddToShoppingCartSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(default=1)

    def create(self, validated_data):
        # Получить идентификатор продукта из проверенных данных
        product_id = validated_data.get('product_id').id

        # Получить пользователя из контекста запроса
        user = self.context['request'].user

        # Получить количество продуктов из проверенных данных
        quantity = validated_data.get('quantity')

        # Создать запись корзины с полученными данными
        shopping_cart_item = ShoppingCart.objects.create(
            user=user,
            product_id=product_id,
            quantity=quantity
        )

        return shopping_cart_item

    def update(self, instance, validated_data):
        new_quantity = validated_data.get('quantity')

        # Обновить количество продуктов в корзине
        instance.quantity = new_quantity
        instance.save()

        return instance