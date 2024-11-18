from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@sky.pro')
        self.lesson = Habit.objects.create(
            user=self.user,
            place='Test place',
            time_when=,
            action='Test action',
            is_pleasant=False,
            regularity=7,
            reward='Мороженое',
            time_to_complete=60,
            is_public=False,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        url = reverse('courses:lessons_create')
        data = {
            'title': 'Тестовый урок 2',
            'video_link': 'https://www.youtube.com/qw',
            'course': self.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_list(self):
        url = reverse('courses:lessons_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)

    def test_lesson_retrieve(self):
        url = reverse('courses:lessons_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.lesson.title)
        self.assertEqual(data.get('course'), self.lesson.course)

    def test_lesson_update(self):
        url = reverse('courses:lessons_update', args=(self.lesson.pk,))
        data = {'title': 'Тестовый урок 3'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Lesson.objects.get(pk=self.lesson.pk).title, 'Тестовый урок 3'
        )

    def test_lesson_delete(self):
        url = reverse('courses:lessons_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

