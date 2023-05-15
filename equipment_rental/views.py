from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import JsonResponse

from .models import Rental
from add_diver.models import Diver


def equipment_rental(request):
    if request.method == "POST":
        # Handle the form submission and create rental objects
        # Update the database accordingly
        # ...

        # Render the receipt page
        context = {
            "rental": rental,  # Pass the rental object to the template
        }
        template = get_template("equipment_rental/rental_receipt.html")
        receipt_html = template.render(context)

        # Generate PDF from the HTML
        pdf_file = generate_pdf(receipt_html)

        # Return the PDF file as a response for download
        response = HttpResponse(content_type="application/pdf")
        response[
            "Content-Disposition"
        ] = 'attachment; filename="Equipment_rental_receipt.pdf"'
        response.write(pdf_file)
        return response
    else:
        # Display the equipment rental form
        # ...
        return render(request, "equipment_rental/rental_form.html")


def generate_pdf(html):
    pdf_file = BytesIO()
    pisa.CreatePDF(html, dest=pdf_file)
    pdf_file.seek(0)
    return pdf_file.getvalue()


def search_divers(request):
    query = request.GET.get("query", "")
    divers = Diver.objects.filter(name__icontains=query).values("id", "name")
    return JsonResponse(list(divers), safe=False)
