from django.urls import path
from . import views

urlpatterns = [
    path("equipment_repair/", views.equipment_repair, name="equipment_repair"),
]
