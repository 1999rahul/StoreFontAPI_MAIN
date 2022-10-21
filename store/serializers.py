from rest_framework import serializers
from decimal import Decimal
from .models import Product,Collection,Customer,Review,CartItem,Cart
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Collection
        fields=['id','title']
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','first_name']
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','title','description','price','inventory','price_with_tax','collection']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')
    def calculate_tax(self, product: Product):
        return product.price*Decimal(1.1)
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['id','name','description','date','product']
class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','title','price','price_with_tax']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')
    def calculate_tax(self, product: Product):
        return product.price*Decimal(1.1)

class CartItemSerializer(serializers.ModelSerializer):
    product=SimpleProductSerializer()
    total_price=serializers.SerializerMethodField(
        method_name='calculate_total_price')
    def calculate_total_price(self,cart_item:CartItem):
        return cart_item.quantity*cart_item.product.price
    class Meta:
        model=CartItem
        fields=['id','product','quantity','total_price']
class CartSerializer(serializers.ModelSerializer):
    id=serializers.UUIDField(read_only=True)
    items=CartItemSerializer(many=True,read_only=True)
    total_cart_price=serializers.SerializerMethodField(
        method_name='calculate_total_cart_price')
    def calculate_total_cart_price(self,cart):
        return sum([item.quantity*item.product.price for item in cart.items.all()])
    class Meta:
        model = Cart
        fields = ['id','items','total_cart_price']
