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
        help_text='Опишите место, отвечая на вопрос "где?"',
    )

    time_where = models.DateTimeField(
        verbose_name='Время',
        blank=True,
        null=True,
        help_text='Опишите место, отвечая на вопрос "когда?"',
    )

    action = models.CharField(
        max_length=50,
        verbose_name='Действие',
        blank=True,
        null=True,
        help_text='Опишите место, отвечая на вопрос "что буду делать?"',
    )

    is_pleasant = models.BooleanField(
        verbose_name='Признак приятной привычки',
        blank=True,
        null=True,
    )

    related_habit = models.ForeignKey(
        'Habit',
        verbose_name='Связанная привычка',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text='Укажите связанную привычку(не указывать, если указали вознаграждение)',
    )

    regularity = models.CharField(
        max_length=50,
        verbose_name='Периодичность(1 раз в __ дней)',
        default='Ежедневно',
        null=True,
    )

    reward = models.CharField(
        max_length=50,
        verbose_name='Вознаграждение',
        blank=True,
        null=True,
        help_text='Укажите вознаграждение(не указывать, если указали связанную привычку)',
    )

    time_to_complete = models.DateTimeField(
        verbose_name='Время на выполнение',
        blank=True,
        null=True
    )

    is_public = models.BooleanField(
        verbose_name='Признак публичности',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Я буду {self.action} в {self.time_where} в {self.place}"

    class Meta:
        db_table = 'habit'
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ()
