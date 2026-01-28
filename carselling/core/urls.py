from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import Login
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('commu/',views.commu,name='commu'),    
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=Login),name='login'),
]
