from django.urls import path
from . import views

urlpatterns = [
     path('', views.home_view, name='home'), 
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profiles/', views.profiles_view, name='profiles'),
    path('about/', views.about_view, name='about'),
]
