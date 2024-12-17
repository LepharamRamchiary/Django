from django import forms
from .models import TeaVarity

class TeaVarityForm(forms.Form):
    tea_varity = forms.ModelChoiceField(queryset=TeaVarity.objects.all(), label="Select Tea varity")