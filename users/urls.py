from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PaymentViewSet


app_name = 'users'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [

] + router.urls
