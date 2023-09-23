from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта ')

    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Номер телефон', **NULLABLE)
    country = models.CharField(max_length=35, verbose_name='Страна', **NULLABLE)
    code = models.PositiveIntegerField(**NULLABLE)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
