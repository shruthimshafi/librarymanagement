
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout



urlpatterns = [

	url(r'^userbooks/$',views.UserBook.userbooks, name='userbooks'),
	url(r'^user_lend/(?P<books_id>\d+)$',views.UserBook.user_lend, name='user_lend'),
	url(r'^userlending/$',views.UserBook.userlending, name='userlending'),
	url(r'^userborrowing/$',views.UserBook.userborrowing, name='userborrowing'),
	url(r'^user_return_request/(?P<books_id>\d+)$',views.UserBook.user_return_request, name='user_return_request'),
	url(r'^userreturning/$',views.UserBook.userreturning, name='userreturning'),
	url(r'^user_review/(?P<books_id>\d+)$',views.UserBook.user_review, name='user_review'),
	url(r'^user_write_review/(?P<book_id>\d+)$',views.UserBook.user_write_review, name='user_write_review'),
	url(r'^borrowing_sucessfull/(?P<books_id>\d+)$',views.UserBook.borrowing_sucessfull, name='borrowing_sucessfull'),
	url(r'^successfuluserlending/$',views.UserBook.successfuluserlending, name='successfuluserlending'),
	
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

