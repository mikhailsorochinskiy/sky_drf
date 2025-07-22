from rest_framework import serializers
from .models import User, Payment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('user',)


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'phone_number', 'avatar', 'city', 'payments')


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Обновляем last_login при успешной аутентификации
        self.user.last_login = timezone.now()
        self.user.save(update_fields=['last_login'])

        return data
