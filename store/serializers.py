from rest_framework import serializers
from decimal import Decimal
from .models import Product,Collection,Customer,Review,CartItem,Cart
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Collection
        fields=['id','title']
class CustomerSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(read_only=True)
    class Meta:
        model=Customer
        fields=['id','user_id','phone','birth_date','membership']
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
class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=['quantity']
class AddCartItemSerializer(serializers.ModelSerializer):
    product_id=serializers.IntegerField()
    class Meta:
        model=CartItem
        fields=['id','product_id','quantity']
    def save(self, **kwargs):
        cart_id=self.context['cart_id']
        product_id=self.validated_data['product_id']
        quantity=self.validated_data['quantity']
        try:
            cart_item=CartItem.objects.get(cart_id=cart_id,product_id=product_id)
            cart_item.quantity+=quantity
            cart_item.save()
            self.instance=cart_item
        except CartItem.DoesNotExist:
           self.instance= CartItem.objects.create(cart_id=cart_id,**self.validated_data)
        return self.instance


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
