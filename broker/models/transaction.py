from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

from .portfolio import Portfolio
from .wallet import Wallet


class TransactionManager(models.Manager):

    def btc(self):
        return super().get_queryset().filter(wallet__symbol='BTC')

    def eth(self):
        return super().get_queryset().filter(wallet__symbol='ETH')

    def ltc(self):
        return super().get_queryset().filter(wallet__symbol='LTC')

    def xrp(self):
        return super().get_queryset().filter(wallet__symbol='XRP')


class Transaction(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, related_name='transactions', null=True, on_delete=models.CASCADE, editable=False)
    wallet = models.ForeignKey(
        Wallet, null=True, on_delete=models.CASCADE, editable=False)
    amount = models.FloatField(editable=False)

    # transaction identifier
    type = models.CharField(max_length=20, blank=True,
                            null=True, editable=False)
    trace_id = models.IntegerField(editable=False, blank=True, null=True)

    # trade specific fields
    profit = models.FloatField(blank=True, null=True, editable=False)
    duration = models.IntegerField(blank=True, null=True, editable=False)

    date_created = models.DateTimeField(default=timezone.now, editable=False)
    withdrawal_date = models.DateTimeField(
        editable=False, blank=True, null=True)

    objects = TransactionManager()

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return str(self.amount) + " " + str(self.type)

    # def save(self, *args, **kwargs):
    #     if self.type == 'buy' or self.type == 'sell' or self.type == 'smart':
    #         span = timedelta(days=self.duration)
    #         if self.date_created is not None:
    #             self.withdrawal_date = self.date_created + span
    #         else:
    #             self.withdrawal_date = timezone.now() + span
    #         if self.profit is None:
    #             self.profit = 0
    #     super(Transaction, self).save(*args, **kwargs)

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
        if self.type == 'buy' or self.type == 'sell' or self.type == 'smart':
            ratio = self.ratio()
            progress = ratio * 100
            return progress

    @property
    def current(self):
        if self.type == 'buy' or self.type == 'sell' or self.type == 'smart':
            ratio = self.ratio()
            current = ratio * self.profit
            return current
