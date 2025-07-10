from rest_framework import serializers
from .models import Course, Lesson
from .validators import VideoURLValidator
from users.models import Subscribe


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoURLValidator(field='video_url')]


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscribe = serializers.SerializerMethodField()

    def get_count_lessons(self, obj):
        return obj.lesson_set.count()

    def get_subscribe(self, obj):
        user = self.context.get("request").user
        if not user.is_authenticated:  # Если пользователь не авторизован
            return False
        return Subscribe.objects.filter(user=user, course=obj).exists()

    class Meta:
        model = Course
        fields = ('id', 'name', 'preview', 'description', 'count_lessons', 'lessons', 'subscribe')
