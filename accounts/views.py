from django.shortcuts import render, render_to_response
from django.http import Http404
from django.http import HttpResponse
from accounts.models import Account


def index(req):
    """Renders homepage for searching Database

    Searches each field currently in database, removing dupes."""
    if req.GET:
        search_term = req.GET['S']
        results = Account.objects.filter(alias__icontains=search_term), \
                  Account.objects.filter(mailbox__icontains=search_term), \
                  Account.objects.filter(type__icontains=search_term), \
                  Account.objects.filter(whitelist_ip__icontains=search_term), \
                  Account.objects.filter(inbox__icontains=search_term), \
                  Account.objects.filter(outbox__icontains=search_term), \
                  Account.objects.filter(host_url__icontains=search_term), \
                  Account.objects.filter(server__icontains=search_term), \
                  Account.objects.filter(customer__icontains=search_term),
        unique = set()
        # TODO: Sorting
        # TODO: Add filter from the results
        # TODO: Add no results page
        # TODO: Dropdown menu
        # TODO: Case sensitvitiy option
        for inquery in results:
            for account in inquery:
                unique.add(account)
        return render_to_response('accounts/index.html', {'results': unique})
    return render_to_response('accounts/index.html', {})

# def index(request):
#     accounts = Account.objects.exclude(type='AS2')
#     return render(request, 'accounts/index.html', {
#         'accounts': accounts,
#     })

def account_detail(request, id):
    """Returns page of Account Details
        Alias
        Mailbox
        Transfer Protocol
        IPs whitelisted
        Paths
        URLS
        Server
        Customer

    :param request:
    :param id:
    :return:
    """
    try:
        account = Account.objects.get(id=id)
    except Account.DoesNotExist:
        raise Http404('This account does not exist')
    return render(request, 'accounts/account_detail.html', {
        'account': account,
    })
