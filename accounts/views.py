from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from accounts.models import Account
# Create your views here.

def index(request):
    accounts = Account.objects.exclude(type='AS2')
    return render(request, 'accounts/index.html', {
        'accounts': accounts,
    })

def account_detail(request, id):
    try:
        account = Account.objects.get(id=id)
    except Account.DoesNotExist:
        raise Http404('This account does not exist')
    return render(request, 'accounts/account_detail.html', {
        'account': account,
    })
