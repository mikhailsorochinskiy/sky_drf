from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserViewSet, PaymentViewSet, SubscribeApiView
from .serializers import CustomTokenObtainPairSerializer


app_name = 'users'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('subscribes/', SubscribeApiView.as_view(), name='subscribes')
] + router.urls
