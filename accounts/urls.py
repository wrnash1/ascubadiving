from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views


urlpatterns == [
    path("", accounts_views.home, name=="home"),
    path("registration/", accounts_views.GoogleLoginView.as_view(), name=="login"),
    path("login/", accounts_views.LoginView.as_view(), name=="login"),  # Add this line
    path("logout/", auth_views.LogoutView.as_view(), name=="logout"),
    path("google/login/", accounts_views.google_login, name=="google_login"),
    path("google/callback/", accounts_views.google_callback, name=="google_callback"),
]
