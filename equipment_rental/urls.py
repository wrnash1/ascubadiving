from django.urls import path
from . import views

urlpatterns = [
    path("equipment_rental/", views.equipment_rental, name="equipment_rental"),
    path(
        "equipment_rental/search_divers/", views.search_divers, name="search_divers"
    ),  # Add this line
]
