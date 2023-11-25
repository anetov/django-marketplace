from django.urls import path
from django.contrib.auth.decorators import login_required
from core.views import MainPage, SignUp, Login, Logout

app_name = 'core'

urlpatterns = [
    path('', MainPage.as_view(), name='mainpage'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
