from django.db import models
from django.conf import settings
# Create your models here.


class SecretPassword(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    secret_password = models.CharField(max_length=255)
