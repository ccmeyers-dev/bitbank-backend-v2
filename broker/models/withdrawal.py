from django.db import models
from django.utils import timezone

from .portfolio import Portfolio
from .wallet import Wallet


class WithdrawalManager(models.Manager):

    def btc(self):
        return super().get_queryset().filter(wallet__symbol='BTC')

    def eth(self):
        return super().get_queryset().filter(wallet__symbol='ETH')

    def ltc(self):
        return super().get_queryset().filter(wallet__symbol='LTC')

    def xrp(self):
        return super().get_queryset().filter(wallet__symbol='XRP')


WALLET_CHOICES = (
    ('BTC', 'BTC'),
    ('ETH', 'ETH'),
    ('LTC', 'LTC'),
    ('XRP', 'XRP'),
)


class Withdrawal(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, related_name='withdrawals', null=True, on_delete=models.CASCADE)
    wallet = models.CharField(
        max_length=10, choices=WALLET_CHOICES, default='BTC')
    amount = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)
    type = models.CharField(
        editable=False, max_length=20, default='withdrawal')

    completed = models.BooleanField(default=False)

    objects = WithdrawalManager()

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return str(self.portfolio) + " " + str(self.amount) + " " + str(self.wallet) + " - Withdrawal"


class Billing(models.Model):
    withdrawal = models.ForeignKey(
        Withdrawal, related_name='billings', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    amount = models.FloatField()

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return str(self.title) + " " + str(self.withdrawal.portfolio)
