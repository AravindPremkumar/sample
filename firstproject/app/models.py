from django.db import models

class Userprofile(models.Model):
    fullname = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
