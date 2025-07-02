from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import User, Payment
from .serializers import UserSerializer, PaymentSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'type')
    ordering_fields = ('payment_date',)
