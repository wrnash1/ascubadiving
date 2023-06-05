from django.urls import path
from .views import gas_blending_view

app_name = "gasblending"

urlpatterns = [
    path("gasblending/", gas_blending_view, name="gas_blending"),
]
