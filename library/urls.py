from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
	url(r'^books/$',views.books, name='books'),
	url(r'^authors/$',views.authors, name='authors'),
	url(r'^lendrequest/$',views.lendrequest, name='lendrequest'),
	url(r'^RequestingDetails/$',views.Requesting, name='RequestingDetails'),
	url(r'^login/$',auth_views.login, name='login'),
	url(r'^signup/$',views.signup, name='signup'),
	url(r'^sucessful_signup/$',views.sucessful_signup, name='sucessful_signup'),
	url(r'^createbook/$',views.createbook, name='createbook'),
    url(r'^addauthor/$',views.addauthor, name='addauthor'),	
	url(r'^auth_view/$',views.auth_view, name='auth_view'),	
	url(r'^invalid_login/$',views.invalid_login, name='invalid_login'),	
	url(r'^logout/$',views.logout, name='logout'),	
	url(r'^approve_lend_request/(?P<lend_id>\d+)$',views.approve_lend_request, name='approve_lend_request'),
	url(r'^reject_lend/(?P<lend_id>\d+)$',views.reject_lend, name='reject_lend'),
	url(r'^approve_return_request/(?P<request_id>\d+)$',views.approve_return_request, name='approve_return_request'),
	url(r'^return_lend/(?P<request_id>\d+)$',views.return_lend, name='return_lend'),
	url(r'^book_details/(?P<books_id>\d+)$',views.book_details, name='book_details'),
	url(r'^user/$', views.user, name='user'),
	url(r'^userbooks/$',views.userbooks, name='userbooks'),
	url(r'^user_lend/(?P<books_id>\d+)$',views.user_lend, name='user_lend'),
	url(r'^borrowing_sucessfull/(?P<books_id>\d+)$',views.borrowing_sucessfull, name='borrowing_sucessfull'),
	url(r'^userlending/$',views.userlending, name='userlending'),
	url(r'^successfuluserlending/$',views.successfuluserlending, name='successfuluserlending'),
	url(r'^userborrowing/$',views.userborrowing, name='userborrowing'),
	url(r'^userreturning/$',views.userreturning, name='userreturning'),
	url(r'^user_return_request/(?P<books_id>\d+)$',views.user_return_request, name='user_return_request'),
	url(r'^user_review/(?P<books_id>\d+)$',views.user_review, name='user_review'),
	url(r'^user_write_review/(?P<book_id>\d+)$',views.user_write_review, name='user_write_review'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

