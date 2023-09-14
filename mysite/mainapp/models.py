from django.db import models

# Create your models here.

class Branchoffice(models.Model):
    def __str__(self):
        return f'{self.city} {self.address}'

    city = models.CharField(max_length=15, verbose_name='city')
    address = models.CharField(max_length=50, verbose_name='address')
    schedule = models.CharField(max_length=50, verbose_name='schedule')
    number = models.CharField(max_length=50, verbose_name='number')


class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    price = models.CharField(max_length=8, verbose_name='price')
    note = models.CharField(max_length=100, verbose_name='note', null=True)


