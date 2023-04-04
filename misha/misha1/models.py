from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Название изделия')

    object = models.Manager


class Detail(models.Model):
    detail_name = models.CharField(max_length=50, verbose_name='Название детали')
    last_name = models.CharField(max_length=50, verbose_name='Описание')
    product = models.CharField(max_length=50, verbose_name='Изделие')

    object = models.Manager


class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя покупателя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')

    object = models.Manager
