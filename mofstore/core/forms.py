from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
  class Meta:
    model=User
    fields=('username','email','password1','password2')
  username=forms.CharField(widget=forms.TextInput(attrs={
    'placeholder':'Enter username',
    'class':'form-control'
  }))
  email=forms.CharField(widget=forms.EmailInput(attrs={
    'placeholder':'Enter email',
    'class':'form-control'
  }))
  password1=forms.CharField(widget=forms.PasswordInput(attrs={
    'class':'form-control'
  }))
  password2=forms.CharField(widget=forms.PasswordInput(attrs={
    'class':'form-control'
  }))
  
class LoginForm(AuthenticationForm):
  username=forms.CharField(widget=forms.TextInput(attrs={
  'placeholder':'Enter username',
  'class':'form-control'
  }))
  password=forms.CharField(widget=forms.PasswordInput(attrs={
  'class':'form-control'
  }))