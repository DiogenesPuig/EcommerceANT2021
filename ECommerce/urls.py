from .views import *
from rest_framework.routers import DefaultRouter

app_name='ECommerce'

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
#router.register(r'supplier', SupplierSerializer, basename='supplier')
urlpatterns = router.urls

