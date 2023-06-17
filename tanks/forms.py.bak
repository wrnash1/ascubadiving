from django import forms
from tanks.models import Tank


class TankForm(forms.ModelForm):
    class Meta:
        model = Tank
        fields = ["name", "capacity", "material"]
