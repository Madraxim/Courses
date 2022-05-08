from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('change-password/', change_password, name='change_password'),
]