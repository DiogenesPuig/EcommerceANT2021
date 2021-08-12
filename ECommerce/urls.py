from .views import *
from rest_framework.routers import DefaultRouter

app_name='ECommerce'

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'suppliers', SupplierViewSet, basename='suppliers')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'deposits', DepositViewSet, basename='deposits')
router.register(r'carts', CartViewSet, basename='carts')
router.register(r'productscarts', ProductsCartViewSet, basename='productscarts')
router.register(r'sales', SaleViewSet, basename='sales')
urlpatterns = router.urls
