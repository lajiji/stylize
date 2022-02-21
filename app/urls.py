from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('', views.login, name='login'),
    path('register/', views.register),
    path('logout/', views.logout),
]