from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.db import models


class Video(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos', validators=[
                             FileExtensionValidator(['mp4', 'avi', 'mov'])])
