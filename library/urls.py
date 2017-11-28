
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout
from .Views.user_view import *
from .Views.admin_view import *
from .Views.authentication_view import *
from .Views import admin_view
from .Views import user_view
from .Views import authentication_view


urlpatterns = [
    url(r'^$',auth_views.login, name='login_new'),
    url(r'^index/$', authentication_view.index, name='index'),
    url(r'^login_new/$',auth_views.login, name='login_new'),
    url(r'^auth_view/$',authentication_view.auth_view, name='auth_view'),
	url(r'^signup_new2/$',authentication_view.signup.as_view(), name='signup_new'),
	url(r'^userbooks/$',user_view.UserBook.userbooks, name='userbooks'),
	url(r'^user_lend/(?P<books_id>\d+)$',user_view.UserBook.user_lend, name='user_lend'),
	url(r'^userlending/$',user_view.UserBook.userlending, name='userlending'),
	url(r'^userborrowing/$',user_view.UserBook.userborrowing, name='userborrowing'),
	url(r'^user_return_request/(?P<books_id>\d+)$',user_view.UserBook.user_return_request, name='user_return_request'),
	url(r'^userreturning/$',user_view.UserBook.userreturning, name='userreturning'),
	url(r'^user_review/(?P<books_id>\d+)$',user_view.UserBook.user_review, name='user_review'),
	url(r'^user_write_review/(?P<book_id>\d+)$',user_view.UserBook.user_write_review, name='user_write_review'),
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
	url(r'^borrowing_sucessfull/(?P<books_id>\d+)$',user_view.UserBook.borrowing_sucessfull, name='borrowing_sucessfull'),
	url(r'^successfuluserlending/$',user_view.UserBook.successfuluserlending, name='successfuluserlending'),
	url(r'^sucessful_signup/$',authentication_view.sucessful_signup, name='sucessful_signup'),
	url(r'^invalid_login/$',authentication_view.invalid_login, name='invalid_login'),	
	url(r'^logout/$',authentication_view.logout, name='logout'),	
	url(r'^user/$', authentication_view.user, name='user'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.conf.urls import url
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import logout
# from .views import signup

# urlpatterns = [
#     url(r'^$',auth_views.login, name='login'),
#     url(r'^index/$', views.index, name='index'),
#     url(r'^login_new/$',auth_views.login, name='login_new'),
#     url(r'^auth_view/$',views.auth_view, name='auth_view'),
# 	url(r'^signup_new/$',signup.as_view(), name='signup_new'),
# 	url(r'^userbooks/$',views.UserBook.userbooks, name='userbooks'),
# 	url(r'^user_lend/(?P<books_id>\d+)$',views.UserBook.user_lend, name='user_lend'),
# 	url(r'^userlending/$',views.UserBook.userlending, name='userlending'),
# 	url(r'^userborrowing/$',views.UserBook.userborrowing, name='userborrowing'),
# 	url(r'^user_return_request/(?P<books_id>\d+)$',views.UserBook.user_return_request, name='user_return_request'),
# 	url(r'^userreturning/$',views.UserBook.userreturning, name='userreturning'),
# 	url(r'^user_review/(?P<books_id>\d+)$',views.UserBook.user_review, name='user_review'),
# 	url(r'^user_write_review/(?P<book_id>\d+)$',views.UserBook.user_write_review, name='user_write_review'),
# 	url(r'^books/$',views.AdminBook.books, name='books'),
# 	url(r'^book_details/(?P<books_id>\d+)$',views.AdminBook.book_details, name='book_details'),
# 	url(r'^createbook/$',views.AdminBook.createbook, name='createbook'),
# 	url(r'^authors/$',views.AdminBook.authors, name='authors'),
# 	url(r'^addauthor/$',views.AdminBook.addauthor, name='addauthor'),
# 	url(r'^lendrequest/$',views.AdminBook.lendrequest, name='lendrequest'),
# 	url(r'^approve_lend_request/(?P<lend_id>\d+)$',views.AdminBook.approve_lend_request, name='approve_lend_request'),
# 	url(r'^reject_lend/(?P<lend_id>\d+)$',views.AdminBook.reject_lend, name='reject_lend'),
# 	url(r'^RequestingDetails/$',views.AdminBook.Requesting, name='RequestingDetails'),
# 	url(r'^approve_return_request/(?P<request_id>\d+)$',views.AdminBook.approve_return_request, name='approve_return_request'),
# 	url(r'^return_lend/(?P<request_id>\d+)$',views.AdminBook.return_lend, name='return_lend'),
# 	url(r'^borrowing_sucessfull/(?P<books_id>\d+)$',views.UserBook.borrowing_sucessfull, name='borrowing_sucessfull'),
# 	url(r'^successfuluserlending/$',views.UserBook.successfuluserlending, name='successfuluserlending'),
# 	url(r'^sucessful_signup/$',views.sucessful_signup, name='sucessful_signup'),
# 	url(r'^sucessful_signup/$',views.sucessful_signup, name='sucessful_signup'),
# 	url(r'^invalid_login/$',views.invalid_login, name='invalid_login'),	
# 	url(r'^logout/$',views.logout, name='logout'),	
# 	url(r'^user/$', views.user, name='user'),
	
	
	
	
	
 
	
	

# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
