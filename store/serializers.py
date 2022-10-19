from rest_framework import serializers
from decimal import Decimal
from .models import Product,Collection,Customer,Review

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
