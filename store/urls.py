from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register('products',views.ProductViewSet)

urlpatterns=router.urls