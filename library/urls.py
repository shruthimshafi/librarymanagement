
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout
from .Views.admin_view import *
from .Views.authentication_view import *
from .Views import admin_view
from .Views import authentication_view

urlpatterns = [
    url(r'^$',auth_views.login, name='login_new'),
    url(r'^index/$', authentication_view.index, name='index'),
    url(r'^login_new/$',auth_views.login, name='login_new'),
    url(r'^auth_view/$',authentication_view.auth_view, name='auth_view'),
	url(r'^signup_new2/$',authentication_view.signup.as_view(), name='signup_new'),
	url(r'^books/$',admin_view.AdminBook.books, name='books'),
	url(r'^book_details/(?P<books_id>\d+)$',admin_view.AdminBook.book_details, name='book_details'),
	url(r'^createbook/$',admin_view.AdminBook.createbook, name='createbook'),
	url(r'^authors/$',admin_view.AdminBook.authors, name='authors'),
	url(r'^addauthor/$',admin_view.AdminBook.addauthor, name='addauthor'),
	url(r'^lendrequest/$',admin_view.AdminBook.lendrequest, name='lendrequest'),
	url(r'^approve_lend_request/(?P<lend_id>\d+)$',admin_view.AdminBook.approve_lend_request, name='approve_lend_request'),
	url(r'^reject_lend/(?P<lend_id>\d+)$',admin_view.AdminBook.reject_lend, name='reject_lend'),
	url(r'^RequestingDetails/$',admin_view.AdminBook.Requesting, name='RequestingDetails'),
	url(r'^approve_return_request/(?P<request_id>\d+)$',admin_view.AdminBook.approve_return_request, name='approve_return_request'),
	url(r'^return_lend/(?P<request_id>\d+)$',admin_view.AdminBook.return_lend, name='return_lend'),
	url(r'^sucessful_signup/$',authentication_view.sucessful_signup, name='sucessful_signup'),
	url(r'^invalid_login/$',authentication_view.invalid_login, name='invalid_login'),	
	url(r'^logout/$',authentication_view.logout, name='logout'),	
	url(r'^user/$', authentication_view.user, name='user'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

