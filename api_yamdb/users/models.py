from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль',
        max_length=32,
        choices=Role.choices,
        default=Role.USER,
    )
    email = models.EmailField(
        'Email',
        unique=True,
        error_messages={
            'unique': 'Пользователь с таким email уже существует.',
        },
    )

    @property
    def is_moderator(self):
        return self.role == self.Role.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser
