from celery import shared_task
from django.core.mail import send_mail

from config import settings
from habits.models import Habit
from users.models import User

import datetime


@shared_task
def reminder_mail(user_id):
    """Отправляем письма об обновлении курса подписчикам курса"""
    user = User.objects.get(pk=user_id)
    habits = Habit.objects.filter(user=user)
    current_time = datetime.datetime.now().strftime('%x %X')

    # for habit in habits:
    #     if
