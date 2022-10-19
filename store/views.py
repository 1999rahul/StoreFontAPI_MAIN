from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
class ProductDetail(APIView):

    def get(self,request,id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def put(self,request,id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def delete(self,request,id):
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductList(ListCreateAPIView):

    def get_queryset(self):
        return Product.objects.all()
    def get_serializer_class(self):
        return ProductSerializer



# Create your views here.
