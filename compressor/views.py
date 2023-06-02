from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import CompressorForm
from diveshopmanagement.models import Compressor, MaintenanceAlert


def compressor_form(request):
    form = CompressorForm()
    if request.method == "POST":
        form = CompressorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("compressor:compressor_detail", id=form.instance.id)
    return render(request, "compressor/compressor_form.html", {"form": form})


def compressor_detail_view(request, id):
    compressor = get_object_or_404(Compressor, id=id)
    context = {"compressor": compressor}
    return render(request, "compressor/compressor_detail.html", context)


def create_compressor(request):
    compressor = Compressor()
    compressor.save()
    return redirect("compressor:compressor_detail", id=compressor.id)


def start_timer(request):
    compressor_id = request.GET.get("compressor_id")
    compressor = get_object_or_404(Compressor, id=compressor_id)
    compressor.date_turned_on = timezone.now()
    compressor.save()
    return redirect("compressor:compressor_detail", id=compressor.id)


def stop_timer(request):
    compressor_id = request.GET.get("compressor_id")
    compressor = get_object_or_404(Compressor, id=compressor_id)
    if compressor.date_turned_on is not None:
        elapsed_time = (timezone.now() - compressor.date_turned_on).total_seconds() / 60
        compressor.minutes += int(elapsed_time)
        compressor.date_turned_on = None
        compressor.save()
    return redirect("compressor:compressor_detail", id=compressor.id)


def reset_filters(request):
    compressor_id = request.GET.get("compressor_id")
    compressor = get_object_or_404(Compressor, id=compressor_id)
    compressor.minutes = 0
    compressor.save()
    return redirect("compressor:compressor_detail", id=compressor.id)


def reset_oil(request):
    compressor_id = request.GET.get("compressor_id")
    compressor = get_object_or_404(Compressor, id=compressor_id)
    compressor.minutes = 0
    compressor.save()
    return redirect("compressor:compressor_detail", id=compressor.id)


def compressor_list(request):
    compressors = Compressor.objects.all()
    compressor_ids = Compressor.objects.values_list("id", flat=True)
    context = {"compressors": compressors, "compressor_ids": list(compressor_ids)}
    return render(request, "compressor/compressor_list.html", context)
