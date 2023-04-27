from django.urls import path
from . import views

urlpatterns = [
    path("equipment_rental/", views.equipment_rental, name="equipment_rental"),
]
