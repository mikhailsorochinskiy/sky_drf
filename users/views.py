from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import User, Payment, Subscribe
from .serializers import UserSerializer, PaymentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from materials.models import Course


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'login']:
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'type')
    ordering_fields = ('payment_date',)


class SubscribeApiView(APIView):
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, id=course_id)

        sub_item = Subscribe.objects.filter(user=user, course=course_item)

        if sub_item.exists():
            sub_item.delete()
            message = 'Подписка удалена'
        else:
            Subscribe.objects.create(user=user, course=course_item)
            message = 'Подписка добавлена'
        return Response({"message": message})
