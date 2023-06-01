from django import forms
from .models import Compressor


class CompressorForm(forms.ModelForm):
    class Meta:
        model = Compressor
        fields = ['minutes', 'notes']
        widgets = {
            'minutes': forms.TextInput(attrs={'readonly': True}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        
class CompressorForm(forms.ModelForm):
    class Meta:
        model = Compressor
        fields = ['notes']