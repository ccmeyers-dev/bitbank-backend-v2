import os
from django.db import models
from .portfolio import Portfolio


def id_front_store(instance, filename):
    name = instance.portfolio.account.first_name.lower(
    ) + '-' + instance.portfolio.account.last_name.lower() + '-' + instance.portfolio.trader_id
    ext = filename.split('.')[-1]
    file = f'front.{ext}'
    return os.path.join('identity', name, file)


def id_back_store(instance, filename):
    name = instance.portfolio.account.first_name.lower(
    ) + '-' + instance.portfolio.account.last_name.lower() + '-' + instance.portfolio.trader_id
    ext = filename.split('.')[-1]
    file = f'back.{ext}'
    return os.path.join('identity', name, file)


class Profile(models.Model):
    portfolio = models.OneToOneField(
        Portfolio, null=True, blank=True, on_delete=models.CASCADE)
    address = models.TextField()
    address2 = models.TextField(null=True, blank=True,)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=20)
    id_front = models.ImageField(
        upload_to=id_front_store, default='noimage.png')
    id_back = models.ImageField(upload_to=id_back_store, default='noimage.png')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return str(self.portfolio) + "'s profile"
