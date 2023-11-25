from django.forms import ModelForm
from .models import Client, Category, Product, Basket
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


INPUT_CLASSES = 'w-100 py-3 px-6 rounded-3'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name_prod', 'description', 'price', 'category','image')
        widgets = { 
            'name_prod': forms.TextInput(attrs={"class": INPUT_CLASSES}),
            'description': forms.TextInput(attrs={"class": INPUT_CLASSES}),
            'price': forms.TextInput(attrs={"class": INPUT_CLASSES}),
            'category': forms.Select(attrs={"class": INPUT_CLASSES}),
            'image': forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }
        
class EditProductForm(ModelForm):
    # captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid':'Неправильный текст'}, generator='captcha.helpers.math_challenge')
    class Meta:
        model = Product
        fields = ('name_prod', 'description', 'price','image', 'is_sold')
        widgets = { 
            'name_prod': forms.TextInput(attrs={"class": INPUT_CLASSES}),
            'description': forms.TextInput(attrs={"class": INPUT_CLASSES}),
            'price': forms.TextInput(attrs={"class": INPUT_CLASSES}),
            'image': forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }
        
