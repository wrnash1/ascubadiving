from django import forms
from add_diver.models import add_diver
from .models import airfill


class AirfillForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=add_diver.objects.all())
    tank_serial_number = forms.CharField(max_length=100)
    visual_date = forms.IntegerField()
    hydro_date = forms.IntegerField()

    class Meta:
        model = airfill
        fields = ["name", "tank_serial_number", "visual_date", "hydro_date"]
