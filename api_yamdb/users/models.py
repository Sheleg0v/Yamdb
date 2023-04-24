from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from .validators import NotEqualValidator

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'
ROLES = (
    (USER, 'Пользователь'),
    (MODERATOR, 'Модератор'),
    (ADMIN, 'Администратор'),
)


class User(AbstractUser):
    username = models.CharField(
        max_length=settings.USER_CHAR_LENGTH,
        unique=True,
        validators=[
            UnicodeUsernameValidator(),
            NotEqualValidator('me')
        ],
        error_messages={
            'unique': ('Пользователь с этим именем уже существует'),
        },
    )
    email = models.EmailField(
        unique=True,
        max_length=settings.EMAIL_CHAR_LENGTH
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль',
        max_length=max([len(role_ru) for role_en, role_ru in ROLES]),
        choices=ROLES,
        default=USER,
    )
    confirmation_code = models.CharField(
        max_length=8,
        default=0,
    )

    @property
    def is_admin(self):
        return self.is_superuser or self.is_staff or self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR
