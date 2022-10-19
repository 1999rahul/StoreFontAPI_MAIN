from rest_framework.viewsets import ModelViewSet
from .models import Product,Review
from .serializers import ProductSerializer,ReviewSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Create your views here.
