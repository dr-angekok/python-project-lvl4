from django.shortcuts import render
from django.utils.translation import gettext as tr


def index(request):
    return render(request, 'index.html', context={
        'tags': tr('List of tags'),
        'users': tr('List of users'),
        'logout': tr('Log out')
    })