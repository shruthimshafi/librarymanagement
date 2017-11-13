from datetime import datetime
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
from .models import Books, Author,Reviews,Photos,FinalUser ,LendingDetails, RequestingDetails
from .forms import AuthorForm ,BooksForm


def hello(request):
    return HttpResponse("Hello world") 

# login view
def login(request):
    """ to login to library """
    c ={}
    return render(
        request,
        'library/login.html', c
    )

# signup view    
def signup(request):
    """ to signup to library """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
    args = {}
    args['form'] = form
    print(args)
    return render(request,"library/signup.html",args)

@login_required(login_url='/login/')    
def addauthor(request):
    """ to add new authors to library """
    if request.method == 'POST':
        print (request.POST)
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/authors/')
        else:
            print (form.errors)
    else:
        form = AuthorForm()
    args = {}
    args['form'] = AuthorForm()
    print(args)
    return render(request, 'library/addauthor.html',args)

    
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
    print(args)
    return render(request, 'library/createbook.html',args)

   
def auth_view(request):
    """ to authenticate users in library 
	check if an user is superuser or not"""
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user.is_superuser:
        auth.login(request,user)
        print('superuser')
        return HttpResponseRedirect('/books/')
    elif user is not None:
        auth.login(request,user)
        id_list = FinalUser.objects.values('user_id')
        print("__________________")
        print("value of userid in FinalUser")
        reg_id=[values['user_id'] for values in id_list]
        print (reg_id)
        flag ='false'
        for search_id in reg_id:
            print("logged in id is",request.user.id,"search id is",search_id)
            if search_id == request.user.id:
                flag ='true'
        if flag == 'false':
            new_user = FinalUser(user_id=request.user.id)
            new_user.save()
            print("New User Added TO fINALuSER")
        else:
            print("User Already Existing")
        print('notsuperuser')
        return HttpResponseRedirect('/userbooks/')
    else:
        return HttpResponseRedirect('/invalid_login/')




def invalid_login(request):
    """ return invalid user """
    return render(request,'library/invalid_login.html')

def sucessful_signup(request):
    """ to show sucessful signup to library """
    return render (request,'library/sucessful_signup.html')

def index(request):
    """ base page for admin """
    print (request.user) 
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
@login_required(login_url='/login/') 
def borrowing_sucessfull(request,books_id):
    """ Message when an book is successfully borrowed by user"""
    id = books_id
    books = Books.objects.get(pk=id)
    photos = Photos.objects.filter(book_id=id)
    details = Books.objects.all()
    current_user = request.user.id
    print('current user',current_user)
    final_user = FinalUser.objects.get(user_id = current_user )
    print('final user',final_user.id)
    lend = LendingDetails(req_date = datetime.now(),req_status='Pending',final_req='On Hold',user_id = final_user.id)
    lend.save()
    lend.books.add(books_id)
    print(lend.req_date)
    #lend.save()
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

@login_required(login_url='/login/') 
def userlending(request):
    """user lending details in library"""
    if request.user.is_authenticated():
        current_user = request.user.id
        final_user = FinalUser.objects.get(user_id = request.user.id)
        lend_id = LendingDetails.objects.filter(user_id=final_user )
        print('lending user-------',lend_id )
        return render(
            request,
            'library/userlending.html',
            {
            'lend':lend_id
            }
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
        print(entry.req_status)
    return render(
        request,
        'library/lendrequest.html', {'details':details}
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

def user_review(request,books_id):
    #details=Books.objects.all()
    print (books_id)
    return render(
        request,
        'library/user_review.html', {'book_id':books_id}
    ) 
def user_write_review(request,book_id):
    """ write review after submiting the book"""
    review_content=request.POST.get('review_content')
    print(review_content)
    final_review=Reviews(review=review_content,book_id=book_id)
    final_review.save()
    return HttpResponseRedirect('/userreturning/')

@login_required(login_url='/login/')
def logout(request):
    """ logout of the library"""
    auth.logout(request)
    return render(
        request,
        'library/logout.html'
    )








    
