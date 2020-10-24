from django.db import models
from django.utils import timezone

from .portfolio import Portfolio


class Notification(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, related_name='notifications', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    message = models.TextField()
    read = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title
