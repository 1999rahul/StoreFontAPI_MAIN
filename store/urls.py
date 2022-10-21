from . import views
from rest_framework_nested import routers

router=routers.DefaultRouter()
router.register('products',views.ProductViewSet)
router.register('cart',views.CartViewSet)

product_router=routers.NestedDefaultRouter(router,'products',lookup='product')
product_router.register('reviews',views.ReviewViewSet,basename='product-reviews')

carts_router=routers.NestedDefaultRouter(router,'cart',lookup='cart')
carts_router.register('items',views.CaerItemViewSet,basename='cart-items')




urlpatterns=router.urls+product_router.urls+carts_router.urls
