from django import forms
from .models import Patient

class PatForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            "fname": forms.TextInput(attrs={"class": "form-control", "placeholder": "First name"}),
            "lname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last name"}),
            "age": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Age"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone"}),
        }
