from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class Sighnupform(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1","password2")

    # class Sighnupform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"Enter username",
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':"Enter your Email",
        'class':'w-full py-4 px-6 rounded-xl',
        
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Enter Password",
        'class':'w-full py-4 px-6 rounded-xl',
        
    }))
    password2 =forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Retype Password",
        'class':'w-full py-4 px-6 rounded-xl',

    }))


class Loginform(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"Enter username",
        'class':'w-full py-4 px-6 rounded-xl',
    }))

    password =forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Enter Password",
        'class':'w-full py-4 px-6 rounded-xl',

    }))