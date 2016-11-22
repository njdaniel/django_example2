from django.contrib import admin

from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ['alias', 'mailbox', 'type', 'whitelist_ip',
                    'inbox', 'outbox', 'host_url', 'server', 'customer']

admin.site.register(Account, AccountAdmin)
