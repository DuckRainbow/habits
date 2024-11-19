import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@sky.pro')
        self.habit = Habit.objects.create(
            user=self.user,
            place='Test place',
            time_when=datetime.datetime.now(),
            action='Test action',
            is_pleasant=False,
            regularity=7,
            reward='Мороженое',
            time_to_complete=60,
            is_public=False,
        )
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Создание привычки"""
        url = reverse('habits:habits_create')
        data = {
            'user': self.user.pk,
            'action': 'Тестовая привычка 2',
            'is_pleasant': 'True',
            'time_when': '2024-11-20T08:10:00Z',
            'place': 'Дом',
            'regularity': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)
        self.assertTrue(Habit.objects.all().exists())

    def test_habit_list(self):
        """Вывод списка привычек"""
        url = reverse('habits:habits_list')
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'action': 'Test action',
                    'related_habit': None,
                    'reward': 'Мороженое',
                    'time_to_complete': 60,
                    'id': self.habit.pk,
                    'is_pleasant': False,
                    'is_public': False,
                    'user': self.user.pk,
                    'regularity': 7,
                    'place': 'Test place',
                    'time_when': datetime.datetime.now(),

                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_retrieve(self):
        """Проверка корректности данных"""
        url = reverse('habits:habits_retrieve', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['place'], self.habit.place)

    def test_habit_update(self):
        """Проверка обновления привычки"""
        url = reverse('habits:habits_update', args=(self.habit.pk,))
        data = {
            'action': 'Тестовая привычка 1 обновлена',
            'regularity': 1,
        }
        response = self.client.patch(url, data, format='json')
        print(response.status_code)
        print(response.__dict__)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['action'], 'Тестовая привычка 1 обновлена')

    def test_habit_delete(self):
        """Проверка удаления привычки"""
        url = reverse('habits:habits_delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)
