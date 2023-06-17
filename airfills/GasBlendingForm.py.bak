from django import forms

class GasBlendingForm(forms.Form):
    oxygen_percentage = forms.DecimalField(
        label='Oxygen (%)',
        min_value=0,
        max_value=100,
        decimal_places=1,
        required=True
    )
    helium_percentage = forms.DecimalField(
        label='Helium (%)',
        min_value=0,
        max_value=100,
        decimal_places=1,
        required=True
    )
    depth = forms.DecimalField(
        label='Depth (meters)',
        min_value=0,
        decimal_places=1,
        required=True
    )
