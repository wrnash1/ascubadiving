from django.urls import path
from blending import views

urlpatterns = [
    path('gas/', views.gas_list, name='gas_list'),
    path('blend/', views.blend_list, name='blend_list'),
]
