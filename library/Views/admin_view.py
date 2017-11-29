from datetime import datetime
#from django.views import View
from django.views.generic import *
from django.shortcuts import render
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


class AdminBook(View):
    @user_passes_test(lambda u: u.is_superuser) 
    @login_required(login_url='/login/')  
    def books(request):
        """ book page in library 
        Shows list of all books library in admin"""
        photo_list = Photos.objects.all()
        details = Books.objects.all()
        authors_list = Author.objects.all()
        paginator = Paginator(details,8)
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
               # If page is not an integer, deliver first page.
            books = paginator.page(1)
        except EmptyPage:
               # If page is out of range (e.g. 9999), deliver last page of results.
            books = paginator.page(paginator.num_pages)
        return render(request, 
            'library/books.html',
            {
            'books_info':books,
            'authors_list':authors_list
            }
            )


    @login_required(login_url='/login/') 
    def book_details(request,books_id):
        """ Show book details of particular book when clicked"""
        id = books_id
        books = Books.objects.get(pk=id)
        photos = Photos.objects.filter(book_id=id)
        author = Author.objects.get(pk=id)
        return render(request, 
            'library/book_details.html',
            {
            'books':books,
            'photos':photos,
            'author':author,
            }
            ) 

    def createbook(request):
        """ to add new books to library """
        if request.method == 'POST':
            print(request.POST)
            form = BooksForm(request.POST, request.FILES)
            book_image = request.FILES.get('photos')
            if form.is_valid():
                s=form.save()
                photos =Photos(photos = book_image, book_id=s.pk)
                photos.save()
                print(photos)
                return HttpResponseRedirect('/books/')
            else:
                print (form.errors)
        else:
            form = BooksForm()
        args = {}
        args['form'] = BooksForm()
        return render(request, 'library/createbook.html',args) 

    @user_passes_test(lambda u: u.is_superuser)
    @login_required(login_url='/login/')    
    def authors(request):
        """ author page in library 
        Shows list of all authors in admin library"""
        authors_list = Author.objects.all()
        paginator = Paginator(authors_list,8)
        page = request.GET.get('page')
        try:
            authors = paginator.page(page)
        except PageNotAnInteger:
               # If page is not an integer, deliver first page.
            authors = paginator.page(1)
        except EmptyPage:
               # If page is out of range (e.g. 9999), deliver last page of results.
            authors = paginator.page(paginator.num_pages)
        return render(request,
         'library/authors.html',
         {
         'authors_list':authors
         }
         )

    @login_required(login_url='/login/')    
    def addauthor(request):
        """ to add new authors to library """
        if request.method == 'POST':
            form = AuthorForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/authors/')
        else:
            form = AuthorForm()
        args = {}
        args['form'] = AuthorForm()
        return render(request, 'library/addauthor.html',args)

        

    @user_passes_test(lambda u: u.is_superuser)
    @login_required(login_url='/login/')    
    def lendrequest(request):
        """ lend request"""
        details = LendingDetails.objects.all()
        return render(
            request,
            'library/lendrequest.html',
            {
            'details':details
            }
        )

    def approve_lend_request(request,lend_id):
        """ approve a lend request by admin"""
        details = LendingDetails.objects.all()
        id=lend_id 
        books = Books.objects.all()
        entry= LendingDetails.objects.get(pk=id)
        entry.final_req = 'Approved'
        entry.save()
        for book in entry.books.all() :
            book.book_count = book.book_count - 1
            book.save()
        if(entry.req_status) != (entry.final_req):   
            entry.req_status = entry.final_req
            entry.save()
        return render(
            request,
            'library/lendrequest.html', {'details':details}
        )
    def reject_lend(request,lend_id):
        """ reject lend details by admin"""
        books = Books.objects.all()
        details = LendingDetails.objects.all()
        id=lend_id
        entry= LendingDetails.objects.get(pk=id)
        entry.final_req = 'Rejected'
        entry.save()
        if(entry.req_status) != (entry.final_req):   
            entry.req_status = entry.final_req
            entry.save()
        return render(
            request,
            'library/lendrequest.html', {'details':details}
        )

    @user_passes_test(lambda u: u.is_superuser)
    @login_required(login_url='/login/')    
    def Requesting(request):
        """ returning books to library"""
        details = RequestingDetails.objects.all() 
        return render(
            request,
            'library/RequestingDetails.html',
            {
            'details':details
            }
        )

    def approve_return_request(request,request_id):
        """ approve lend details by admin"""
        books = Books.objects.all()
        details = RequestingDetails.objects.all()
        id = request_id
        entry= RequestingDetails.objects.get(pk=id)   
        entry.final_status = 'Received'
        entry.save()
        for book in entry.books.all() :
            book.book_count = book.book_count + 1
            book.save()
        if(entry.status) != (entry.final_status):   
            entry.status = entry.final_status
            entry.save()
        return render(
            request,
            'library/RequestingDetails.html', {'details':details}
        )

    def return_lend(request,request_id):
        """ return lended book back to library"""
        details = RequestingDetails.objects.all()
        id = request_id
        entry= RequestingDetails.objects.get(pk=id)  
        entry.final_status = 'Not Received'
        entry.save()
        if(entry.status) != (entry.final_status):   
            entry.status = entry.final_status
            entry.save()
        return render(
            request,
            'library/RequestingDetails.html', {'details':details}
        )
