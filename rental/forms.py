from django import forms
from diveshopmanagement.models import Rental


class RentalForm(forms.ModelForm):
    class Meta:
        model == Rental
        fields == ["item", "customer", "rental_date", "return_date"]
