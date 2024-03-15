from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Изображение (превью)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', **NULLABLE,
                                 related_name='categories')
    price = models.FloatField(verbose_name='Цена за покупку')
    created_at = models.DateField(verbose_name='Дата создания (записи в БД)')
    updated_at = models.DateField(verbose_name='Дата последнего изменения (записи в БД)')
    manufactured_at = models.DateField(verbose_name='Дата производства продукта', **NULLABLE )

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
