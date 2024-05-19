from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Login(models.Model):
    user_name = models.CharField(max_length=20)
    hash_password = models.TextField()
    
class Register(models.Model):
    email = models.EmailField(max_length=100)
    contact = models.TextField(max_length = 10)
    
    class Meta:
        pass