"""Functions used by celery to be run async can also be scheduled"""

from __future__ import absolute_import, unicode_literals
import csv
from celery import shared_task

from accounts.models import Account

@shared_task
def import_csv():
    """Imports csv into the accounts.models for each Account

    This function is be run on a schedule. During the
        """
    # print(listdir)
    path_to_csv =  './accounts/all.csv'
    with open(path_to_csv) as f:
        reader = csv.reader(f)
        for row in reader:
            obj, created = Account.objects.get_or_create(
                alias=row[0],
                mailbox=row[1],
                type=row[2],
                whitelist_ip=row[3],
                inbox=row[4],
                outbox=row[5],
                host_url=row[6],
                server=row[7],
                customer=row[8],
            )