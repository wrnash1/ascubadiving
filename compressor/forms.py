from django import forms
from diveshopmanagement.models import Compressor


class CompressorForm(forms.ModelForm):
    class Meta:
        model = Compressor
        fields = "__all__"  # Or specify the fields you want to include in the form
