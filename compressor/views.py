from django.shortcuts import render, redirect, get_object_or_404
from diveshopmanagement.models import Compressor
from .forms import CompressorForm
from .utils import calculate_elapsed_time
from django.http import HttpResponse
from django.utils import timezone


def compressor_form(request):
    compressor = Compressor.objects.first()
    if request.method == "POST":
        if "start" in request.POST:
            if not compressor.date_turned_on:
                compressor.date_turned_on = timezone.now()
                compressor.save()
        elif "stop" in request.POST:
            if compressor.date_turned_on:
                time_diff = timezone.now() - compressor.date_turned_on
                minutes = int(time_diff.total_seconds() / 60)
                compressor.minutes += minutes
                compressor.date_turned_on = None
                compressor.save()
                if compressor.check_air_filter_alert():
                    # Show air filter alert
                    pass
                if compressor.check_oil_change_alert():
                    # Show oil change alert
                    pass
    return render(
        request, "compressor/compressor_form.html", {"compressor": compressor}
    )


def start_timer(request):
    if request.method == "POST":
        form = CompressorForm(request.POST)
        if form.is_valid():
            compressor = form.save(commit=False)
            compressor.start_time = datetime.now()
            compressor.save()
            return redirect("compressor:timer")
    else:
        form = CompressorForm()

    return render(request, "compressor/start_timer.html", {"form": form})


def stop_timer(request):
    compressor = Compressor.objects.last()
    if compressor and compressor.start_time:
        minutes = calculate_elapsed_time(compressor.start_time)
        compressor.minutes += minutes
        compressor.start_time = None
        compressor.save()

    return redirect("compressor:timer")


def compressor_detail_view(request):
    compressor_id = request.GET.get("id")

    if compressor_id is None:
        # Handle the case when the compressor ID is not provided
        return render(request, "compressor/compressor_not_found.html")

    compressor = get_object_or_404(Compressor, pk=compressor_id)

    return render(
        request, "compressor/compressor_detail.html", {"compressor": compressor}
    )
