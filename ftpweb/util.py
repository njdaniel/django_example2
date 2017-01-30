# from __future__ import absolute_import, unicode_literals
# import csv, os, sys
# from os import listdir
#
# from accounts.models import Account
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ftpweb.settings')
#
# def import_csv(path_to_csv):
#     """Imports csv into the accounts.models for each Account
#     """
#     print(listdir)
#     with open(path_to_csv) as f:
#         reader = csv.reader(f)
#         for row in reader:
#             obj, created = Account.objects.get_or_create(
#                 alias = row[0],
#                 mailbox = row[1],
#                 type = row[2],
#                 whitelist_ip = row[3],
#                 inbox = row[4],
#                 outbox = row[5],
#                 host_url = row[6],
#                 server = row[7],
#                 customer = row[8],
#             )
# import_csv('all.csv')