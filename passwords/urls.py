from rest_framework.routers import DefaultRouter
from .views import PasswordViewSet

router = DefaultRouter()
router.register('', PasswordViewSet, basename='password')

urlpatterns = router.urls
