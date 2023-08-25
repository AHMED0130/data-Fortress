from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Video
from .serializers import VideoSerializer
# Create your views here.


class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Video.objects.filter(user_id=self.request.user.id)

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}
