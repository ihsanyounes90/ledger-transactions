from django.db import models


class Transaction(models.Model):
    name = models.TextField()
    referer = models.TextField()
    amount = models.FloatField()
    balance = models.FloatField()
    date = models.DateTimeField()
