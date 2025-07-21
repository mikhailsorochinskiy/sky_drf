from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from .permissions import IsModerator, IsOwner
from rest_framework.permissions import AllowAny, IsAuthenticated
from .paginators import ListPagination
from materials.tasks import send_mail_update_course
from users.models import Subscribe


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = ListPagination

    def get_permissions(self):
        if self.action in ['update', 'retrieve']:
            return [IsModerator(), IsOwner()]
        if self.action == 'destroy':
            return [IsOwner()]
        if self.action == 'create':
            self.permission_classes = (~IsModerator,)
            return super().get_permissions()
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderators').exists():
            return Course.objects.all()
        return Course.objects.filter(owner=self.request.user)

    def perform_update(self, serializer):
        """Отсылает сообщение об обновлении курса подписанному пользователю"""
        course = serializer.save()
        subs = Subscribe.objects.filter(course=course)
        recipients = []
        for sub in subs:
            recipients.append(sub.user.email)
        send_mail_update_course.delay(recipients, course.name)


class LessonListApiView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = ListPagination
    # permission_classes = [IsModerator]

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderators').exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonCreateApiView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [~IsModerator]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()

class LessonRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonUpdateApiView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonDestroyApiView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]
