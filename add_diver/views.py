from django.shortcuts import render, redirect
from .models import Diver


def add_diver(request):
    if request.method == "POST":
        certification_number = request.POST.get("certification_number")

        try:
            # Search for the diver in the database based on the certification number
            diver = Diver.objects.get(certification_number=certification_number)
            # Fill the form fields with the diver's data
            return render(request, "add_diver.html", {"diver": diver})
        except Diver.DoesNotExist:
            # If the diver is not found, proceed with creating a new diver
            name = request.POST.get("name")
            certification_level = request.POST.get("certification_level")
            certification_agency = request.POST.get("certification_agency")
            date_of_birth = request.POST.get("date_of_birth")
            dan_insurance = request.POST.get("dan_insurance")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            address = request.POST.get("address")
            zipcode = request.POST.get("zipcode")
            shirt_size = request.POST.get("shirt_size")

            # Create a new Diver object with the submitted data
            diver = Diver(
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

    # Render the form template if it's a GET request or if the diver was not found
    return render(request, "add_diver.html")
