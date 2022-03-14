from email.headerregistry import Address
from importlib.metadata import requires
from pickle import TRUE
from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    Address = models.TextField(max_length=200)

    def __str__(self):
        return(self.username)

