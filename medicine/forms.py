from django import forms
from .models import medicine

class medicineForm(forms.ModelForm):
    class Meta:
        model = medicine
        fields = ['MedicineName','Description','ExpiryDate','Price']