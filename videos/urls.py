from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from .views import VideoViewSet

router = DefaultRouter()
router.register('', VideoViewSet, basename='video')

urlpatterns = router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
