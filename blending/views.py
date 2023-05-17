from django.shortcuts import render
from .models import Gas, Blend

def gas_list(request):
    gases = Gas.objects.all()
    return render(request, 'blending/gas_list.html', {'gases': gases})

def blend_list(request):
    blends = Blend.objects.all()
    return render(request, 'blending/blend_list.html', {'blends': blends})
