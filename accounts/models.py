from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=2000)
    type = models.CharField(max_length=2000)
    host = models.CharField(max_length=2000)
    server = models.CharField(max_length=2000)