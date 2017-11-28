from datetime import datetime
#from django.views import View
from django.views.generic import *
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from library.models import Books, Author,Reviews,Photos,FinalUser ,LendingDetails, RequestingDetails
from library.forms import AuthorForm ,BooksForm



class Authentication (View):
    def login(request):
        """ to login to library """
        c ={}
        return render(
            request,
            'library/login.html', c
        )

class signup(View):
    def post(self, request):
        
        """ to signup to library """
        form = UserCreationForm(request.POST)
        print('form unsuccessful!!!!!!')
        if form.is_valid():
            form.save()
            print('form success!!!!!!')
            return HttpResponseRedirect('/login_new/')
    def get(self, request):
        print('form gettt!!!!!!')
        form = UserCreationForm()
        print('form gettt!!!!!!')
        args = {}
        args['form'] = form
        return render(request,"library/new_signup.html",args)

   
def auth_view(request):
    """ to authenticate users in library 
	check if an user is superuser or not"""
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    # if user.is_superuser:
    #     auth.login(request,user)
    #     return HttpResponseRedirect('/books/')
    if user is not None:
        auth.login(request,user)
        id_list = FinalUser.objects.values('user_id')
        reg_id=[values['user_id'] for values in id_list]
        flag ='false'
        for search_id in reg_id:
                flag ='true'
        if flag == 'false':
            new_user = FinalUser(user_id=request.user.id)
            new_user.save()
        else:
            print("User already exist")
        if user.is_superuser:
            return HttpResponseRedirect('/books/')
        else:
            return HttpResponseRedirect('/userbooks/')

    else:
        messages.error(request, 'Invalid Credentials')
        return HttpResponseRedirect('/invalid_login/')


def invalid_login(request):
    """ return invalid user """
    return render(request,'library/invalid_login.html')

def sucessful_signup(request):
    """ to show sucessful signup to library """
    return render (request,'library/sucessful_signup.html')

def index(request):
    """ base page for admin """
    return render(
        request,
        'library/index.html'
    )

def user(request):
    """ base page for user """
    return render(
        request,
        'library/user.html'
    )

@login_required(login_url='/login/')
def logout(request):
    """ logout of the library"""
    auth.logout(request)
    return render(
        request,
        'library/logout.html'
    )








    
