from django import forms
from .models import ZayavkaModel

class ZayavkaForm(forms.ModelForm):
    class Meta:
        model = ZayavkaModel
        fields = '__all__'
