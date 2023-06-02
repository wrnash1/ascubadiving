from django.urls import path
from . import views

app_name = "compressor"

urlpatterns = [
    path("form/", views.compressor_form, name="compressor_form"),
    path("compressor/detail/", views.compressor_detail_view, name="compressor_detail"),
    path("create/", views.compressor_form, name="create_compressor"),
]
