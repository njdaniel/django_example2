from django.shortcuts import render, render_to_response
from django.http import Http404
from django.http import HttpResponse
from accounts.models import Account


def index(req):
    if req.GET:
        search_term = req.GET['S']
        results = Account.objects.filter(alias__contains=search_term)
        return render_to_response('accounts/index.html', {'results': results})
    return render_to_response('accounts/index.html', {})

# def index(request):
#     accounts = Account.objects.exclude(type='AS2')
#     return render(request, 'accounts/index.html', {
#         'accounts': accounts,
#     })

def account_detail(request, id):
    try:
        account = Account.objects.get(id=id)
    except Account.DoesNotExist:
        raise Http404('This account does not exist')
    return render(request, 'accounts/account_detail.html', {
        'account': account,
    })
