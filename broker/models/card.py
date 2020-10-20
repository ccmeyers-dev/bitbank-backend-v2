from django.db import models
from .portfolio import Portfolio


class Card(models.Model):
    portfolio = models.OneToOneField(
        Portfolio, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    card_number = models.CharField(max_length=30)
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()
    cvv = models.IntegerField()
    ssn = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return str(self.first_name) + "'s card"
