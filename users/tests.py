from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from .models import User, Subscribe
from materials.models import Course


class SubscribeAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.course = Course.objects.create(name='test', description='test')
        self.client.force_authenticate(user=self.user)

    def test_post_create(self):
        url = reverse('users:subscribes')
        data = {
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("message"), 'Подписка добавлена')
        self.assertTrue(Subscribe.objects.filter(user=self.user, course=self.course).exists())

    def test_post_delete(self):
        Subscribe.objects.create(user=self.user, course=self.course)
        url = reverse('users:subscribes')
        data = {
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("message"), 'Подписка удалена')
        self.assertFalse(Subscribe.objects.filter(user=self.user, course=self.course).exists())

    def test_subscribe_to_nonexistent_course(self):
        """Тестирование добавления подписки на несуществующий курс"""
        url = reverse("users:subscribes")
        response = self.client.post(url, {"course": 1000000})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
