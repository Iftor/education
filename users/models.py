from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


# class UserPosition(models.Model):
#     class Meta:
#         verbose_name = 'User position'
#         verbose_name_plural = 'User positions'
#
#     name = models.CharField(max_length=50, unique=True, verbose_name='Position name')
#
#     def __str__(self):
#         return self.name


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    # position = models.ForeignKey(
    #     to='users.UserPosition',
    #     on_delete=models.SET_NULL,
    #     related_name='users',
    #     null=True,
    #     verbose_name='Position',
    # )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        # return f'{self.last_name} {self.first_name} ({self.position})'
        return f'{self.last_name} {self.first_name}'
