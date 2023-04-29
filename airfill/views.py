from django.shortcuts import render
from django.http import HttpResponse

def airfill(request):
    if request.method == "POST":
        name = request.POST["name"]
        tank_serial_number = request.POST["tank_serial_number"]
        visual_date = request.POST["visual_date"]
        hydro_date = request.POST["hydro_date"]
        airfill = Airfill(name=name, tank_serial_number=tank_serial_number, visual_date=visual_date, hydro_date=hydro_date)
        airfill.save()
        return HttpResponse("Airfill added successfully!")
    return render(request, "airfill.html")
