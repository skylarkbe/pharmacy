from django import forms
from django.utils.translation import gettext as _trans

from .models import Pharmaceutical
from .constants import MEDICINE_TO_ICON, MEDICINE_DEFAULT_ICON, DATE_INPUT_FORMATS


class IconWithLabelElement:
    # This class generates a simple HTML output to link an ionIcon and a text together
    def __init__(self, label, icon):
        self.label = label
        self.icon = icon

    def __str__(self):
        return "<i class='icon " + self.icon + "'></i><span>" + self.label + '</span>'


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


class AddMedicineForm(forms.Form):
    inputPharmaceutical = forms.ModelChoiceField(
        required=True,
        queryset=Pharmaceutical.objects.all().order_by('name'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    inputMedicalType = forms.ChoiceField(
        required=True,
        choices=(
            ("Pill", IconWithLabelElement(
                label=_trans("Pill"),
                icon=MEDICINE_TO_ICON.get("Pill", MEDICINE_DEFAULT_ICON))),
            ("Syrup", IconWithLabelElement(
                label=_trans("Syrup"),
                icon=MEDICINE_TO_ICON.get("Syrup", MEDICINE_DEFAULT_ICON))),
            ("Bandage", IconWithLabelElement(
                label=_trans("Bandage"),
                icon=MEDICINE_TO_ICON.get("Bandage", MEDICINE_DEFAULT_ICON))),
            ("Tool", IconWithLabelElement(
                label=_trans("Tool"),
                icon=MEDICINE_TO_ICON.get("Tool", MEDICINE_DEFAULT_ICON))),
        ),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )
    inputExpirationDate = forms.DateField(
        required=True,
        input_formats=DATE_INPUT_FORMATS,
        widget=forms.HiddenInput()
    )
    medicineNeverExpires = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'value': 'True'})
    )
    inputAmount = forms.IntegerField(
        required=True,
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control','value': 1, 'aria-describedby': 'inputAmountHelper'})
    )
    inputValidity = forms.IntegerField(
        required=False,
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 1, 'aria-describedby': 'inputValidityHelp'})
    )
    inputSterility = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'value': 'True'})
    )
