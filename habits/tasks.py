from celery import shared_task
from habits.models import Habit
from users.models import User

import datetime


@shared_task
def reminder_mail(user_id):
    """Отправляем письма об обновлении курса подписчикам курса"""
    user = User.objects.get(pk=user_id)
    habits = Habit.objects.filter(user=user, is_pleasant=False)
    current_time = datetime.datetime.now().strftime('%x %X')

    for habit in habits:
        habit_time = datetime.datetime.strftime(habit.time_when, '%x %X')
        if habit_time == current_time:
            message = f'Сейчас запланировано выполнение {habit.action} в {habit.place}. \nВремя на выполнение: {habit.time_to_complete}.\n'
            if habit.related_habit:
                message += f'После выполнения можете наградить себя: {habit.related_habit}'
            else:
                message += f'После выполнения можете наградить себя: {habit.reward}'
