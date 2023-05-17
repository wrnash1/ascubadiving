from django.urls import path
from . import views

app_name = "compressor"

urlpatterns = [
    path("", views.compressor_list, name="compressor_list"),
]
