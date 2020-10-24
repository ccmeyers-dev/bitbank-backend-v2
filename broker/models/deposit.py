from django.db import models
from django.utils import timezone

from .portfolio import Portfolio
from .wallet import Wallet


class DepositManager(models.Manager):

    def btc(self):
        return super().get_queryset().filter(wallet__symbol='BTC')

    def eth(self):
        return super().get_queryset().filter(wallet__symbol='ETH')

    def ltc(self):
        return super().get_queryset().filter(wallet__symbol='LTC')

    def xrp(self):
        return super().get_queryset().filter(wallet__symbol='XRP')


class Deposit(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, related_name='deposits', null=True, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, null=True, on_delete=models.CASCADE)
    amount = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)
    type = models.CharField(editable=False, max_length=20, default='deposit')

    objects = DepositManager()

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return str(self.amount) + " - Deposit"
