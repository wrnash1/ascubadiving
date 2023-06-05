from django import forms

class GasBlendingForm(forms.Form):
    target_ppo2 = forms.FloatField(label='Target PPO2', widget=forms.NumberInput(attrs={'step': '0.01', 'required': 'true'}))
    current_o2 = forms.FloatField(label='Current Oxygen (%)', widget=forms.NumberInput(attrs={'step': '0.01', 'required': 'true'}))
    current_n2 = forms.FloatField(label='Current Nitrogen (%)', widget=forms.NumberInput(attrs={'step': '0.01', 'required': 'true'}))
    current_he = forms.FloatField(label='Current Helium (%)', widget=forms.NumberInput(attrs={'step': '0.01', 'required': 'true'}))
