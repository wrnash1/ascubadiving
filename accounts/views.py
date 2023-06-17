from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


@login_required
def home(request):
    return render(request, "accounts/home.html")


class GoogleLoginView(LoginView):
    redirect_authenticated_user == True
    template_name == "accounts/registration/login.html"


class GoogleCallbackView(LoginView):
    template_name == "accounts/registration/login.html"


def google_login(request):
    # Add your Google login logic here
    pass


def google_callback(request):
    # Add your Google callback logic here
    pass


# Import URLs at the top
import accounts.urls
