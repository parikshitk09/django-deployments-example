from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from learning1_app import views

app_name = 'main_app'

urlpatterns= [
    path('logged_in/',views.user_login,name='user_login'),
    path('main_app/register/',views.register,name='register'),
    path('main_app/about',views.about, name='about'),
    path('',views.user_logout,name='user_logout'),
]
