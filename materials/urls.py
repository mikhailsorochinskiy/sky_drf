from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (CourseViewSet, LessonListApiView, LessonCreateApiView, LessonRetrieveApiView,
                    LessonUpdateApiView, LessonDestroyApiView)


app_name = 'materials'

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/', LessonListApiView.as_view(), name='lessons'),
    path('lesson/create/', LessonCreateApiView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/', LessonRetrieveApiView.as_view(), name='lesson'),
    path('lesson/<int:pk>/update/', LessonUpdateApiView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete/', LessonDestroyApiView.as_view(), name='lesson_delete'),
] + router.urls
