from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Account(models.Model):
    alias = models.CharField(max_length=2000)
    mailbox = models.CharField(max_length=2000)
    type = models.CharField(max_length=2000)
    whitelist_ip = models.CharField(max_length=2000)
    inbox = models.CharField(max_length=2000)
    outbox = models.CharField(max_length=2000)
    host_url = models.CharField(max_length=2000)
    server = models.CharField(max_length=2000)
    customer = models.CharField(max_length=2000)

# TODO: When account was created
# TODO: Who created the account
# TODO: Actions of accounts