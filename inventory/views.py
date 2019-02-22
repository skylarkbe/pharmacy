from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _trans

from datetime import datetime

from .models import Medicine, Pharmaceutical, Pill, Syrup, Tool, Bandage
from .forms import AddPharmaceuticalForm, AddMedicineForm


def index(request):
    all_stock = Medicine.objects.all().select_subclasses()
    return render(request, 'inventory/index.html', {'all_stock': all_stock})


class AddPharmaceuticalView(TemplateView):
    template_name = "inventory/addPharmaceutical.html"

    def get(self, request, *args, **kwargs):
        add_pharmaceutical = AddPharmaceuticalForm()
        return render(request, self.template_name, {'add_pharmaceutical_form': add_pharmaceutical})

    def post(self, request, *args, **kwargs):
        method_decorator(csrf_protect)
        add_pharmaceutical = AddPharmaceuticalForm(request.POST)
        if add_pharmaceutical.is_valid():
            new_pharmaceutical = Pharmaceutical(
                name=add_pharmaceutical.cleaned_data['inputPharmaceuticalName'],
                medicalPrescription=add_pharmaceutical.cleaned_data['requiresMedicalPrescription']
            )
            new_pharmaceutical.save()
            if new_pharmaceutical.id is not None:
                messages.add_message(
                    request, messages.SUCCESS,
                    _trans("The pharmaceutical has been successfully created."),
                    extra_tags='alert-success'
                )
            else:
                messages.add_message(
                    request, messages.ERROR,
                    _trans("The pharmaceutical was not created."),
                    extra_tags='alert-danger'
                )
            return redirect('inventory:index')
        else:
            messages.add_message(
                request, messages.ERROR,
                _trans("There are errors in the submitted form."),
                extra_tags='alert-danger'
            )
            return render(request, self.template_name, {'add_pharmaceutical_form': add_pharmaceutical})


class AddMedicineView(TemplateView):
    template_name = "inventory/addMedicine.html"

    def get(self, request, *args, **kwargs):
        add_medicine = AddMedicineForm()
        return render(request, self.template_name, {'add_medicine_form': add_medicine})

    def post(self, request, *args, **kwargs):
        method_decorator(csrf_protect)
        add_medicine = AddMedicineForm(request.POST)
        if add_medicine.is_valid():
            input_medical_type=add_medicine.cleaned_data['inputMedicalType']
            if input_medical_type == "Pill":
                pill = Pill(
                    type=add_medicine.cleaned_data['inputPharmaceutical'],
                    amount=add_medicine.cleaned_data['inputAmount'],
                    insertDate=datetime.now(),
                    expirationDate=add_medicine.cleaned_data['inputExpirationDate'],
                )
                pill.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    _trans("The pill has been successfully added to your pharmacy."),
                    extra_tags='alert-success'
                )
            elif input_medical_type == "Syrup":
                syrup = Syrup(
                    type=add_medicine.cleaned_data['inputPharmaceutical'],
                    amount=add_medicine.cleaned_data['inputAmount'],
                    insertDate=datetime.now(),
                    expirationDate=add_medicine.cleaned_data['inputExpirationDate'],
                    validity=add_medicine.cleaned_data['inputValidity']
                )
                syrup.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    _trans("The syrup has been successfully added to your pharmacy."),
                    extra_tags='alert-success'
                )
            elif input_medical_type == "Bandage":
                bandage = Bandage(
                    type=add_medicine.cleaned_data['inputPharmaceutical'],
                    amount=add_medicine.cleaned_data['inputAmount'],
                    insertDate=datetime.now(),
                    expirationDate=add_medicine.cleaned_data['inputExpirationDate'],
                    is_sterile=add_medicine.cleaned_data['inputSterility'],
                )
                bandage.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    _trans("The bandage has been successfully added to your pharmacy."),
                    extra_tags='alert-success'
                )
            elif input_medical_type == "Tool":
                tool = Tool(
                    type=add_medicine.cleaned_data['inputPharmaceutical'],
                    amount=add_medicine.cleaned_data['inputAmount'],
                    insertDate=datetime.now(),
                    expirationDate=add_medicine.cleaned_data['inputExpirationDate'],
                    is_sterile=add_medicine.cleaned_data['inputSterility'],
                )
                tool.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    _trans("The tool has been successfully added to your pharmacy."),
                    extra_tags='alert-success'
                )
            else:
                messages.add_message(
                    request, messages.ERROR,
                    _trans("The chosen medicine type is not known, please select a valid type."),
                    extra_tags='alert-danger'
                )
            return redirect('inventory:index')
        else:
            messages.add_message(
                request, messages.ERROR,
                _trans("There are errors in the submitted form."),
                extra_tags='alert-danger'
            )
            return render(request, self.template_name, {'add_medicine_form': add_medicine})
