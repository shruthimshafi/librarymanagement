from django.contrib import admin
from .models  import Books, Author, Photos, Reviews, FinalUser, LendingDetails, RequestingDetails , User


# Register your models here.
admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Photos)
admin.site.register(Reviews)
admin.site.register(FinalUser)
admin.site.register(LendingDetails)
admin.site.register(RequestingDetails)