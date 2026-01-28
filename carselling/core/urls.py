from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('commu/',views.commu,name='commu'),
    path('signup/',views.signup,name='signup')
]
