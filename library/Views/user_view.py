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

class UserBook(ListView):
    def userbooks(request):
        """ book page in library 
        Shows list of all books library in user"""
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
               # If page is out olibrarynge (e.g. 9999), deliver last page of results.
            books = paginator.page(paginator.num_pages)
        return render(request, 
            'library/userbooks.html',
            {
            'books_info':books,
            'authors_list':authors_list,
            }
            )
    #@login_required(login_url='/login/') 
    def user_lend(request,books_id):
        """ Show lend details of specific user"""
        id = books_id
        books = Books.objects.get(pk=id)
        photos = Photos.objects.filter(book_id=id)
        return render(request, 
            'library/user_lend.html',
            {
            'books':books,
            'photos':photos,
            }
            )
    @login_required(login_url='/login/') 
    def userlending(request):
        """user lending details in library"""
        if request.user.is_authenticated():
            current_user = request.user.id
            final_user = FinalUser.objects.get(user_id = request.user.id)
            lend_id = LendingDetails.objects.filter(user_id=final_user )
            return render(
                request,
                'library/userlending.html',
                {
                'lend':lend_id
                }
            )

    @login_required(login_url='/login/') 
    def userborrowing(request):
        """ user borrowing"""
        if request.user.is_authenticated():
            current_user = request.user.id
            final_user = FinalUser.objects.get(user_id = request.user.id)
            lend_id = LendingDetails.objects.filter(user_id=final_user )

        return render(
            request,
            'library/userborrowing.html',
            {
            'lend':lend_id
             }
        )

    def user_return_request(request,books_id):
        """user return request"""
        if request.user.is_authenticated():
            current_user = request.user.id
            final_user = FinalUser.objects.get(user_id = request.user.id)
            return_id = RequestingDetails.objects.filter(user_id=final_user)
            lend = LendingDetails.objects.filter(user_id=final_user)
            id = books_id
            returning = RequestingDetails(date = datetime.now(),status='Pending',final_status='On Hold',user_id = final_user.id)
            returning.save()
            returning.books.add(books_id)
            return render(
                request,
                'library/successfuluserlending.html',
                {'lend':lend}
            )

    @login_required(login_url='/login/') 
    def userreturning(request):
        """return book back to library """
        if request.user.is_authenticated():
            current_user = request.user.id
            final_user = FinalUser.objects.get(user_id = request.user.id)
            return_id = RequestingDetails.objects.filter(user_id=final_user )
        return render(
            request,
            'library/userreturning.html',
            {
            'returning':return_id
            }
        )

    def user_review(request,books_id):

        return render(
            request,
            'library/user_review.html', {'book_id':books_id}
        )

    def user_write_review(request,book_id):
        """ write review after submiting the book"""
        review_content=request.POST.get('review_content')
        final_review=Reviews(review=review_content,book_id=book_id)
        final_review.save()
        return HttpResponseRedirect('/userreturning/')

    @login_required(login_url='/login/') 
    def borrowing_sucessfull(request,books_id):
        """ Message when an book is successfully borrowed by user"""
        id = books_id
        books = Books.objects.get(pk=id)
        photos = Photos.objects.filter(book_id=id)
        details = Books.objects.all()
        current_user = request.user.id
        final_user = FinalUser.objects.get(user_id = current_user )
        lend = LendingDetails(req_date = datetime.now(),req_status='Pending',final_req='On Hold',user_id = final_user.id)
        lend.save()
        lend.books.add(books_id)
        paginator = Paginator(details,8)
        page = request.GET.get('page')
        try:
            book = paginator.page(page)
        except PageNotAnInteger:
               # If page is not an integer, deliver first page.
            book = paginator.page(1)
        except EmptyPage:
               # If page is out olibrarynge (e.g. 9999), deliver last page of results.
            book = paginator.page(paginator.num_pages)
        return render(request, 
            'library/borrowing_sucessfull.html',
            {
            'books':books,
            'books_info':details,
            'photos':photos,
            'books_info':book,
            'lend':lend,
            }
            ) 

    def successfuluserlending(request):
        """ message to show if a book is successfully lend"""
        if request.user.is_authenticated():
            current_user = request.user.id
            final_user = FinalUser.objects.get(user_id = request.user.id)
            lend = LendingDetails.objects.filter(user_id=final_user)
            return render(
                request,
                'library/successfuluserlending.html',
                {
                'lend':lend
                }
            )