from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Debit(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    is_gain = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)