from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

from .portfolio import Portfolio
from .wallet import Wallet


class TradeManager(models.Manager):

    def btc(self):
        return super().get_queryset().filter(wallet__symbol='BTC')

    def eth(self):
        return super().get_queryset().filter(wallet__symbol='ETH')

    def ltc(self):
        return super().get_queryset().filter(wallet__symbol='LTC')

    def xrp(self):
        return super().get_queryset().filter(wallet__symbol='XRP')


TRADE_CHOICES = (
    ('buy', 'buy'),
    ('sell', 'sell'),
    ('smart', 'smart'),
)


class Trade(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, related_name='trades', null=True, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, null=True, on_delete=models.CASCADE)
    amount = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        max_length=20, choices=TRADE_CHOICES, default='buy')
    profit = models.FloatField(blank=True, null=True)
    duration = models.IntegerField()
    withdrawal_date = models.DateTimeField(
        editable=False, blank=True, null=True)

    objects = TradeManager()

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return str(self.amount) + " - Trade"

    def save(self, *args, **kwargs):
        span = timedelta(days=self.duration)
        if self.date_created is not None:
            self.withdrawal_date = self.date_created + span
        else:
            self.withdrawal_date = timezone.now() + span
        if self.profit is None:
            self.profit = 0
        super(Trade, self).save(*args, **kwargs)

    def ratio(self):
        withdate = self.date_created + timedelta(days=self.duration)
        elapsed = timezone.now() - self.date_created
        span = withdate - self.date_created
        ratio = elapsed / span
        if ratio > 1:
            ratio = 1
        return ratio

    @property
    def progress(self):
        ratio = self.ratio()
        progress = ratio * 100
        return progress

    @property
    def current(self):
        ratio = self.ratio()
        current = ratio * self.profit
        return current
