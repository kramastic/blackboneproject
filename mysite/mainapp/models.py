


from django.db import models

# Create your models here.

class Branchoffice(models.Model):
    def __str__(self):
        return f'{self.city} {self.address}'


    city = models.ForeignKey('City', on_delete=models.PROTECT, null=False)
    address = models.CharField(max_length=50, verbose_name='address')
    metro_station =models.CharField(max_length=50, verbose_name='metro', null=True)
    schedule = models.CharField(max_length=50, verbose_name='schedule')
    number = models.CharField(max_length=50, verbose_name='number')
    telegram = models.CharField(max_length=200, verbose_name='telegram', null=True)
    inst = models.CharField(max_length=200, verbose_name='inst', null=True)
    vk = models.CharField(max_length=200, verbose_name='vk', null=True)

class City(models.Model):
    city = models.CharField(max_length=50, verbose_name='city')

class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    price = models.CharField(max_length=8, verbose_name='price')
    note = models.CharField(max_length=100, verbose_name='note', null=True)