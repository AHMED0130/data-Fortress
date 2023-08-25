from rest_framework import serializers
from .models import SecretPassword
from cryptography.fernet import Fernet
from django.conf import settings
import base64

# Generate a Fernet key
fernet_key = Fernet.generate_key()

# Encode the key to make it URL-safe
encoded_key = base64.urlsafe_b64encode(fernet_key)


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretPassword
        fields = ['id', 'title', 'secret_password']

    def encrypt_password(self, password):
        cipher_suite = Fernet(encoded_key)
        encrypted_password = cipher_suite.encrypt(password.encode())
        return encrypted_password.decode()

    def decrypt_password(self, encrypted_password):
        cipher_suite = Fernet(encoded_key)
        decrypted_password = cipher_suite.decrypt(encrypted_password.encode())
        return decrypted_password.decode()

    def create(self, validated_data):
        user_id = self.context.get('user_id')
        validated_data['secret_password'] = self.encrypt_password(
            validated_data['secret_password']
        )
        instance = SecretPassword.objects.create(
            user_id=user_id, **validated_data)
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['secret_password'] = self.decrypt_password(
            representation['secret_password']
        )
        return representation
