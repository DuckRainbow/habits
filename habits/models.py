from django.db import models

from users.models import User


class Habit(models.Model):
  user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

  place = models.CharField(
        max_length=50,
        verbose_name='Место',
        blank=True,
        null=True,
    )

  time_where = models.DateTimeField(
        verbose_name="Время",
        blank=True,
        null=True
    )

  action = models.CharField(
        max_length=50,
        verbose_name='Действие',
        blank=True,
        null=True,
    )

  is_pleasant = models.BooleanField()

  related_habit = models.ForeignKey(
        User,
        verbose_name='Связанная привычка',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

  regularity =

  reward = models.CharField(
        max_length=50,
        verbose_name='Вознаграждение',
        blank=True,
        null=True,
    )

  time_to_complete = models.DateTimeField(
        verbose_name="Время на выполнение",
        blank=True,
        null=True
    )

  is_public = models.BooleanField()