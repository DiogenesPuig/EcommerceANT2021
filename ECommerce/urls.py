from .views import *
from rest_framework.routers import DefaultRouter

app_name='ECommerce'

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'suppliers', ClientViewSet, basename='suppliers')
router.register(r'products', ClientViewSet, basename='products')
router.register(r'deposits', ClientViewSet, basename='deposits')
router.register(r'carts', ClientViewSet, basename='carts')
router.register(r'productscarts', ClientViewSet, basename='productscarts')
router.register(r'sales', ClientViewSet, basename='sales')
#router.register(r'supplier', SupplierSerializer, basename='supplier')
urlpatterns = router.urls

