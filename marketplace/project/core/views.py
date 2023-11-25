from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, View

from products.models import Category, Product
from .forms import LoginForm, SignUpForm

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Create your views here.
class MainPage(ListView):
    model = Product
    template_name = 'main/main.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавьте ваш дополнительный параметр в контекст
        categories = Category.objects.all()
        context['categories'] = categories
        return context
    

class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('core:login')
    
class Login(LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'
    next_page = 'core:mainpage'
    
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('mainpage'))
        else:
            return super().get(request, *args, **kwargs)
        
class Logout(LogoutView):
    next_page = 'core:mainpage'