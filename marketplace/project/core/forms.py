from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=15, required=True, widget = forms.TextInput(attrs={"class": "w-100 py-3 px-6 rounded-2"}))
    password = forms.CharField(max_length=15, required=True, widget = forms.PasswordInput(attrs={"class": "w-100 py-3 px-6 rounded-2"}))
    
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={"class": "w-100 py-3 px-3 rounded-2"}),
        }
        
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(max_length=15, required=True, widget = forms.PasswordInput(attrs={"class": "w-100 py-3 px-6 rounded-2"}))
    password2 = forms.CharField(max_length=15, required=True, widget = forms.PasswordInput(attrs={"class": "w-100 py-3 px-6 rounded-2"}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={"class": "w-100 py-3 px-3 rounded-2"}),
            'email': forms.EmailInput(attrs={"class": "w-100 py-3 px-3 rounded-2"}),
        }