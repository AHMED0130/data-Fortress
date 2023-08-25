from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import images
from .serializers import ImageSerializer
# Create your views here.


class ImageViewSet(ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return images.objects.filter(user_id=self.request.user.id)

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}
