from django.contrib import admin
from django.urls import path
from myapp import views 


urlpatterns = [
    path("", views.index, name='index'),
    path("signup", views.handleSignup, name='handleSignup'),
    path("login", views.handleLogin, name='handleLogin'),
    path("logout", views.handleLogout, name='handleLogout'),
    path("contact", views.Contact, name='Contact'),
    path('usercheck', views.usercheck, name='usercheck'),
    path('challenges', views.challenges, name='challenges'),
    path('quiz', views.quiz, name='quiz'),
    path('PostAnswer', views.PostAnswer, name='PostAnswer'),
    path('<str:link>', views.quizcontent, name='quizcontent'),
]
