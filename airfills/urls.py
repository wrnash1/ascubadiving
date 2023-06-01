from django.urls import path, include
from . import views

app_name = "airfills"

urlpatterns = [
    path("", views.airfill_list, name="airfill_list"),
    path("<int:pk>/", views.airfill_detail, name="airfill_detail"),
    path("create/", views.airfill_create, name="airfill_create"),
    path("<int:pk>/update/", views.airfill_update, name="airfill_update"),
    path("<int:pk>/delete/", views.airfill_delete, name="airfill_delete"),
]

