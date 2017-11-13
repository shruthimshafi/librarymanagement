from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
BOOK_STATUS = (
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Rejected','Rejected'),
    )

FINAL_STATUS = (
            ('Approved','Approved'),
            ('Rejected','Rejected'),
            )
REQ_STATUS = (
            ('Received','Received'),
            ('Not Not Received','Not Received'),
            )

FINAL_REQ_STATUS = (
            ('Received','Received'),
            ('Not Received','Not Received'),
            ) 

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    place_of_birth = models.CharField(max_length=100, null=True)
    author_photo = models.ImageField(null=True)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)
        
class Books(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ManyToManyField(Author)
    publication_date = models.DateField()
    description = models.TextField(max_length = 500)
    rating = models.FloatField()
    book_count = models.IntegerField(null=True)

    def __str__(self):
        return u'%s ' % (self.title)    
class Photos(models.Model):
    photos = models.ImageField(null=True)
    book = models.ForeignKey(Books, null=True,related_name='newphotos')

    def __str__(self):
        return u'%s ' % (self.book_id)

class Reviews(models.Model):
    review = models.TextField(max_length=500, null=True)
    book = models.ForeignKey(Books, null=True, related_name='reviews')

    def __str__(self):
        return u'%s ' % (self.book_id)
    

# class NewUser(models.Model):
    # user = models.OneToOneField(User,max_length=100)
    # phone_regex = models.RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    # email = models.EmailField(max_length= 100,null=True)

    # def __str__(self):
        # return u'%s ' % (self.user)
        
class FinalUser(models.Model):
    user = models.OneToOneField(User,max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    email = models.EmailField(max_length= 100,null=True)

    def __str__(self):
         return u'%s ' % (self.user)

class RequestingDetails(models.Model):
    books = models.ManyToManyField(Books)
    date = models.DateField()
    status = models.CharField(choices=REQ_STATUS,max_length=30)
    final_status = models.CharField(choices=FINAL_REQ_STATUS,max_length=30,null=True)
    user = models.ForeignKey(FinalUser,null=False)


    def __str__(self):
        return u'%s ' % (self.date)
        
class LendingDetails(models.Model):
    books = models.ManyToManyField(Books)
    req_date = models.DateField()
    req_status = models.CharField(choices=BOOK_STATUS,max_length=30)
    final_req = models.CharField(choices=FINAL_STATUS,max_length=30,null=True)
    user = models.ForeignKey(FinalUser,null=False)
    
    def __str__(self):
        return u'%s ' % (self.req_date)









    
