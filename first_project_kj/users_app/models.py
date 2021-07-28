from django.db import models
from datetime import datetime, time


class Users(models.Model):
    email = models.EmailField(primary_key=True,unique=True, max_length=200)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)

# remanmes the instance of the model as the fname
    def __str__(self):
        return self.lname
