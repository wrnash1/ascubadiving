from django.urls import path, include
from . import views

app_name = "compressor"

urlpatterns = [
    path("compressor/form/", views.compressor_form, name="compressor_form"),
    path(
        "compressor/detail/<int:id>/",
        views.compressor_detail_view,
        name="compressor_detail",
    ),
    path("compressor/create/", views.create_compressor, name="create_compressor"),
    path("compressor/start_timer/", views.start_timer, name="start_timer"),
    path("compressor/stop_timer/", views.stop_timer, name="stop_timer"),
    path("compressor/reset_filters/", views.reset_filters, name="reset_filters"),
    path("compressor/reset_oil/", views.reset_oil, name="reset_oil"),
    path("compressor/list/", views.compressor_list, name="compressor_list"),
]
