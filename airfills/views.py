from django.shortcuts import render, get_object_or_404, redirect
from diveshopmanagement.models import Airfill


def airfill_list(request):
    airfills = Airfill.objects.all()
    return render(request, "airfills/airfill_list.html", {"airfills": airfills})


def airfill_detail(request, pk):
    airfill = get_object_or_404(Airfill, pk=pk)
    return render(request, "airfills/airfill_detail.html", {"airfill": airfill})


def airfill_create(request):
    if request.method == "POST":
        # Process the form data and create a new Airfill object
        # ...
        return redirect("airfills:airfill_list")
    else:
        return render(request, "airfills/airfill_create.html")


def airfill_update(request, pk):
    airfill = get_object_or_404(Airfill, pk=pk)
    if request.method == "POST":
        # Process the form data and update the existing Airfill object
        # ...
        return redirect("airfills:airfill_detail", pk=airfill.pk)
    else:
        return render(request, "airfills/airfill_update.html", {"airfill": airfill})


def airfill_delete(request, pk):
    airfill = get_object_or_404(Airfill, pk=pk)
    if request.method == "POST":
        # Delete the Airfill object
        airfill.delete()
        return redirect("airfills:airfill_list")
    else:
        return render(request, "airfills/airfill_confirm_delete.html", {"airfill": airfill})
