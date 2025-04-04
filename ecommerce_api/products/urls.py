from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet)

urlpatterns = router.urls
