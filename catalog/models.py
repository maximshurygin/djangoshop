from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                             related_name='products', **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)
    change_date = models.DateTimeField(auto_now=True, verbose_name='дата изменения', **NULLABLE)

    def get_current_version(self):
        return self.version_set.filter(is_current_version=True).first()

    def __str__(self):
        return f'{self.name}: {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=100, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    is_current_version = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return self.version_name

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
