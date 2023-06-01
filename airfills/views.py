from django.shortcuts import render, get_object_or_404, redirect
from diveshopmanagement.models import Airfill
from .forms import AirfillForm


def airfill_create(request):
    if request.method == "POST":
        form = AirfillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("airfills:airfill_list")
    else:
        form = AirfillForm()
    return render(request, "airfills/airfill_create.html", {"form": form})


def airfill_list(request):
    airfills = Airfill.objects.all()
    return render(request, "airfills/airfill_list.html", {"airfills": airfills})


def airfill_detail(request, pk):
    airfill = get_object_or_404(Airfill, pk=pk)
    return render(request, "airfills/airfill_detail.html", {"airfill": airfill})


def airfill_update(request, pk):
    airfill = get_object_or_404(Airfill, pk=pk)
    if request.method == "POST":
        form = AirfillForm(request.POST, instance=airfill)
        if form.is_valid():
            form.save()
            return redirect("airfills:airfill_detail", pk=airfill.pk)
    else:
        form = AirfillForm(instance=airfill)
    return render(
        request, "airfills/airfill_update.html", {"form": form, "airfill": airfill}
    )


def airfill_delete(request, pk):
    airfill = get_object_or_404(Airfill, pk=pk)
    if request.method == "POST":
        airfill.delete()
        return redirect("airfills:airfill_list")
    return render(request, "airfills/airfill_confirm_delete.html", {"airfill": airfill})


#def tank_create(request):
#    tank_create = Tank.objects.create(
#        tank_identifier=tank.tank_identifier,
#        size=tank.size,
#        location=tank.location,
#        hydro_dropoff_date=tank.hydro_dropoff_date,
#        hydro_pickup_date=tank.hydro_pickup_date,
#        hydro_passed=tank.hydro_passed,
#    )
#    return render(request, "airfills/tank_create.html")
