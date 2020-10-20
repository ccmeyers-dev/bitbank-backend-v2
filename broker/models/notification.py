from django.db import models
from .portfolio import Portfolio


class Notification(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, related_name='notifications', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title
