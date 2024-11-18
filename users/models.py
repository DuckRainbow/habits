from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )
    token = models.CharField(
        max_length=100,
        verbose_name='Token',
        blank=True,
        null=True,
    )
    phone_num = models.IntegerField(
        verbose_name='Phone',
        blank=True,
        null=True,
    )
    telegram_id = models.CharField(
        max_length=100,
        verbose_name="telegram_id",
        help_text="Введите ID чата",
        blank=True,
        null=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ('can_block_user', 'Can block user')
        ]

    def __str__(self):
        return self.email