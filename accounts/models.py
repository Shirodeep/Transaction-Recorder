from django.db import models
class Login(models.Model):
    user_name = models.CharField(max_length=20)
    hash_password = models.TextField()
