from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

ROLES = [
        ('Пользователь', 'user'),
        ('Модератор', 'moder'),
        ('Админ', 'admin'),
]


class MyUser(AbstractUser):
    bio = models.CharField(_('bio'), max_length=256, blank=True)
    role = models.CharField(
        _('role'),
        max_length=28,
        choices=ROLES,
        default='Пользователь'
    )
