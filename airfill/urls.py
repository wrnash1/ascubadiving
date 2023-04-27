from django.urls import path
from . import views

urlpatterns = [
    path("airfill/", views.airfill, name="airfill"),
]
