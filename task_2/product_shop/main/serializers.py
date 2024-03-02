from rest_framework import serializers
from config import settings
from main.models import Category, SubCategory, Product, ShoppingCart, ShoppingCartItem
from rest_framework.exceptions import ValidationError


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
        fields = ['id', 'name', 'category', 'subcategory', 'price', 'image']


class ShoppingCartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = ShoppingCartItem
        fields = ['id', 'product', 'quantity']

class ShoppingCartSerializer(serializers.ModelSerializer):
    items = ShoppingCartItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ['user', 'items']


    def to_representation(self, instance):
        '''Метод для вывода информации об общей суммы корзины и кол-во товаров'''
        representation = super().to_representation(instance)
        total_items = sum(item.quantity for item in instance.items.all())
        total_cost = sum(item.product.price * item.quantity for item in instance.items.all())
        representation['total_items'] = total_items
        representation['total_cost'] = total_cost
        return representation



class AddToShoppingCartSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(default=1)

    def create(self, validated_data):
        '''Создание товара в корзине'''
        user = self.context['request'].user
        product_id = validated_data.get('product_id').id
        quantity = validated_data.get('quantity')

        # Получаем корзину для пользователя
        shopping_cart, created = ShoppingCart.objects.get_or_create(user=user)

        # Проверяем, есть ли товар уже в корзине
        if ShoppingCartItem.objects.filter(cart=shopping_cart, product_id=product_id).exists():
            raise ValidationError("Товар уже находится в корзине")

        # Создаем новый элемент корзины
        shopping_cart_item = ShoppingCartItem.objects.create(
            cart=shopping_cart,
            product_id=product_id,
            quantity=quantity
        )

        return shopping_cart_item

class UpdateShoppingCartItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()

    def update(self, instance, validated_data):
        '''Обновление данных элемента корзины'''
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
