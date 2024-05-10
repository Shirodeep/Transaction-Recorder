from django.db import models
# Create your models here.

class Debit(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    is_gain = models.IntegerField()
