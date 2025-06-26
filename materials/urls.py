from rest_framework.routers import DefaultRouter
from .views import CourseViewSet


app_name = 'materials'

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [

] + router.urls