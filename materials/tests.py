from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Lesson, Course
from users.models import User

# Create your tests here.
class LessonApiTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.course = Course.objects.create(name='test', description='test')
        self.lesson = Lesson.objects.create(name='test', description='test', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_get(self):
        url = reverse('materials:lesson', args=[self.lesson.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), self.lesson.name)

    def test_create(self):
        url = reverse('materials:lesson_create')
        data = {"name": "new test",
                "description": "new test",
                "course": self.course.pk,
                }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_update(self):
        url = reverse('materials:lesson_update', args=[self.lesson.pk])
        data = {
            "name": "test update"
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), "test update")

    def test_delete(self):
        url = reverse('materials:lesson_delete', args=[self.lesson.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_list(self):
        url = reverse('materials:lessons')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.all().count(), 1)
