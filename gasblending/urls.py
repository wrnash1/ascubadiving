from django.urls import path
from gasblending.views import gas_blending_view

app_name = "gasblending"

urlpatterns = [
    path("", gas_blending_view, name="gas_blending"),
]
