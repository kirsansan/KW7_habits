from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager

# from main.models import NULLABLE

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email', unique=True)
    phone = models.CharField(max_length=35, verbose_name='phone', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='country', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)
    last_name = models.CharField(verbose_name='last name', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} aka {self.last_name if self.last_name else 'unknown'}"

    # @property
    # def username(self):
    #     return self.user.email


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
