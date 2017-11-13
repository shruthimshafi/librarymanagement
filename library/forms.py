from django import forms
from django.forms import ModelForm
from library.models import Author,Books

class MyRegistrationForm(forms.Form):
    email = forms.EmailField(required = True)
    password = forms.CharField(required = True)

class MySignupForm(forms.Form):
    email = forms.EmailField(required = True)
    password = forms.CharField(required = True, widget = forms.PasswordInput)
    confirm_password = forms.CharField(required = True, widget = forms.PasswordInput)
    age = forms.IntegerField(required = True)

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name','last_name','age','place_of_birth','author_photo']

	
class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title','author','publication_date','description','rating','book_count']