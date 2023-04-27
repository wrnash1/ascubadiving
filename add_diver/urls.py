from django.urls import path
from . import views

urlpatterns = [
    path("add_diver/", views.add_diver, name="add_diver"),
]
