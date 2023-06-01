from django.urls import path
from . import views

app_name = 'compressor'

urlpatterns = [
    path('form/', views.compressor_form, name='compressor_form'),
]
