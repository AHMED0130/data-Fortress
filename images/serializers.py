from rest_framework import serializers
from .models import images


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = images
        fields = ['id', 'image']

    def create(self, validated_data):
        user_id = self.context['user_id']
        instance = images.objects.create(
            user_id=user_id, **self.validated_data)
        return instance
