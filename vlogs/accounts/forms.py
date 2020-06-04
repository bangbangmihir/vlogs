from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,label = 'First Name')
    last_name = forms.CharField(max_length=100,label='Last Name')
    email = forms.EmailField(max_length=100,label = 'Email')
    phone = forms.CharField(max_length=13,label='Phone no.')

    class Meta:
        model = User
        fields = ['username','first_name','last_name','phone','email','password1','password2']
