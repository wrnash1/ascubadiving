from django.shortcuts import render
from .models import Compressor

def compressor_list(request):
    compressors = Compressor.objects.all()
    return render(request, 'compressor/compressor_list.html', {'compressors': compressors})
