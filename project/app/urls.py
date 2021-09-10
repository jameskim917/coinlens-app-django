from rest_framework import routers
from .views import TransactionViewSet

router = routers.DefaultRouter()
router.register('transactions', TransactionViewSet, basename='transactions')

urlpatterns = router.urls