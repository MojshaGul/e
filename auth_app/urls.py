from django.contrib import admin
from django.urls import path
from auth_app.views import register, login, logout

urlpatterns = [
    path('register/', register, name="register_page"),
    path('login/', login, name="login_page"),
    path('logout/', logout, name="logout_page"),
]