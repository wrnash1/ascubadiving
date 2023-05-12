from django.shortcuts import render, redirect
from .models import add_diver

# def add_diver(request):
#    # Code to handle the admin/add_divers URL goes here
#    return render(request, "add_diver.html")


def add_diver(request):
    if request.method == "POST":
        name = request.POST.get("name")
        certification_number = request.POST.get("certification_number")
        certification_level = request.POST.get("certification_level")
        certification_agency = request.POST.get("certification_agency")
        date_of_birth = request.POST.get("Date_of_birth")
        dan_insurance = request.POST.get("Dan_insurance")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        zipcode = request.POST.get("zipcode")
        shirt_size = request.POST.get("shirt_size")

        # Create a new Diver object with the submitted data
        diver = add_diver(
            name=name,
            certification_number=certification_number,
            certification_level=certification_level,
            certification_agency=certification_agency,
            date_of_birth=date_of_birth,
            dan_insurance=dan_insurance,
            email=email,
            phone=phone,
            address=address,
            zipcode=zipcode,
            shirt_size=shirt_size,
        )

        # Save the diver object to the database
        diver.save()

        # Redirect to a success page or do any additional processing
        return redirect("success_page")

    # Render the form template if it's a GET request
    return render(request, "add_diver.html")
