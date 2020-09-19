from django.db import models


class Wallet(models.Model):
    wallet = models.CharField(max_length=20)
    symbol = models.CharField(max_length=4, default='')
    address = models.CharField(max_length=100, default='Coming Soon')

    def __str__(self):
        return self.symbol
