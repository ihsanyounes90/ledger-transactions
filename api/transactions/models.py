from django.db import models


class Transaction(models.Model):
    name = models.TextField(db_index=True)
    referer = models.TextField()
    amount = models.FloatField()
    balance = models.FloatField()
    date = models.DateTimeField(db_index=True)
