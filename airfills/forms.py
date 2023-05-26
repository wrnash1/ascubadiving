from django import forms
from diveshopmanagement.models import Airfill


class AirfillForm(forms.ModelForm):
    class Meta:
        model = Airfill
        fields = ["date", "fill_pressure", "oxygen_percentage"]
