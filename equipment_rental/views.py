# from django.shortcuts import render


# def equipment_rental(request):
#    return render(request, "equipment_rental.html")


from django.shortcuts import render, redirect
from .models import Equipment, Rental, RentalEquipment



def equipment_rental(request):
    if request.method == "POST":
        # Process equipment rental form submission
        form_data = request.POST
        diver_id = form_data.get("diver")
        start_date = form_data.get("start_date")
        end_date = form_data.get("end_date")
        items = form_data.getlist("item[]")
        rental_prices = form_data.getlist("rental_price[]")
        deposits = form_data.getlist("deposit[]")
        rental_insurances = form_data.getlist("rental_insurance[]")
        rental_insurance_prices = form_data.getlist("rental_insurance_price[]")
        rental_totals = form_data.getlist("rental_total[]")

        diver = add_diver_models.add_diver.objects.get(id=diver_id)

        rental = Rental.objects.create(
            diver=diver, date_of_rental=start_date, date_due=end_date
        )

        for (
            item,
            rental_price,
            deposit,
            rental_insurance,
            rental_insurance_price,
            rental_total,
        ) in zip(
            items,
            rental_prices,
            deposits,
            rental_insurances,
            rental_insurance_prices,
            rental_totals,
        ):
            equipment = Equipment.objects.get(id=item)
            rental_equipment = RentalEquipment.objects.create(
                rental=rental,
                equipment=equipment,
                rental_price=rental_price,
                deposit=deposit,
                rental_insurance=rental_insurance,
                rental_insurance_price=rental_insurance_price,
                rental_total=rental_total,
            )
            equipment.available = False  # Update equipment availability
            equipment.save()

        return redirect("equipment_rental")  # Redirect after successful submission

    equipment = Equipment.objects.filter(available=True)
    divers = add_diver_models.add_diver.objects.all()

    context = {"equipment": equipment, "divers": divers}

    return render(request, "equipment_rental.html", context)
