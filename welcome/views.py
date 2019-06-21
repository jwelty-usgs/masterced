from django.shortcuts import *
from django.http import *
from accounts.views import checkgroup

def index(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'welcome/index.html', context)
    else:
        return render(request, 'welcome/index.html')

def faq(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'welcome/faq.html', context)
    else:
        return render(request, 'welcome/faq.html')   

def news(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}

    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'welcome/news.html', context)
    else:
        return render(request, 'welcome/news.html')

def about(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'welcome/about.html', context)
    else:
        return render(request, 'welcome/about.html')

def help(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen, 'showlogin':'True'}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'welcome/help.html',  context)
    else:
        return render(request, 'welcome/help.html',  context)

def statemods(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'welcome/statemods.html', context)
    else:
        return render(request, 'welcome/statemods.html')

def dst(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'welcome/dst.html', context)
    else:
        return render(request, 'welcome/dst.html')

def under_construction(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'welcome/under_construction.html', context)
    else:
        return render(request, 'welcome/under_construction.html')
