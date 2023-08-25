from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video']

    def create(self, validated_data):
        user_id = self.context['user_id']
        instance = Video.objects.create(
            user_id=user_id, **self.validated_data)
        return instance
