from django import forms
from django.utils.translation import gettext as _trans


class AddPharmaceuticalForm(forms.Form):
    inputPharmaceuticalName = forms.CharField(
        required=True,
        max_length=128,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _trans('Pharmaceutical name')})
    )
    requiresMedicalPrescription = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'value': 'True'})
    )
