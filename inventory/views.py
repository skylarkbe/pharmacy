from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _trans

from datetime import datetime

from .constants import APPLICATION_FILTERS, MEDICINE_TYPE_FILTERS
from .forms import AddPharmaceuticalForm, AddMedicineForm
from .models import Medicine, Pharmaceutical, Pill, Syrup, Tool, Bandage


def index(request):
    type_filters=active_type_filters(request)
    validity_filters=active_validity_filters(request)

    search_term=request.GET['search'] if 'search' in request.GET else ""

    all_stock_types = Medicine.objects.filter(
        subtype__in=type_filters,
        type__name__icontains=search_term
    ).select_subclasses()

    sub_stock = [obj for obj in all_stock_types if obj.is_medicine_expired() in validity_filters]

    return render(request, 'inventory/index.html', {'all_stock': sub_stock, 'input_search': search_term})


def toggle_filter(request):
    filter_name = request.GET['filter']
    if filter_name in APPLICATION_FILTERS:
        if request.session.get(filter_name, True):
            request.session[filter_name] = False
        else:
            request.session[filter_name] = True
    return redirect('inventory:index')


def active_type_filters(request):
    active_filter = []
    for filter_name in MEDICINE_TYPE_FILTERS:
        if request.session.get(filter_name, True):
            active_filter.append(filter_name)
    return active_filter


def active_validity_filters(request):
    active_filter = []
    if request.session.get('show_not_expired', True):
        active_filter.append(False)
    if request.session.get('show_expired', True):
        active_filter.append(True)
    return active_filter


def open_syrup(request):
    medicine_id=request.GET['id'] if 'id' in request.GET else None
    if medicine_id:
        syrup=Syrup.objects.get(id=medicine_id)
        if syrup:
            syrup.openedDate=datetime.now()
            syrup.save()
    return redirect('inventory:index')


def add_stock_unit(request):
    medicine_id = request.GET['id'] if 'id' in request.GET else None
    if medicine_id:
        medicine=Medicine.objects.get(id=medicine_id)
        if medicine:
            medicine.amount=medicine.amount+1
            medicine.save()
            return HttpResponse(medicine.amount, content_type="text/plain")
    return HttpResponseNotFound(medicine_id)


def remove_stock_unit(request):
    medicine_id = request.GET['id'] if 'id' in request.GET else None
    if medicine_id:
        medicine=Medicine.objects.get(id=medicine_id)
        if medicine:
            if medicine.amount > 0:
                medicine.amount=medicine.amount-1
                medicine.save()
                return HttpResponse(medicine.amount, content_type="text/plain")
            else:
                medicine.delete()
                return HttpResponse("DELETE", content_type="text/plain")
    return HttpResponseNotFound(medicine_id)


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
            input_medical_type = add_medicine.cleaned_data['inputMedicalType']
            if input_medical_type == "Pill":
                pill = Pill(
                    subtype='show_pills',
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
                    subtype='show_syrups',
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
                    subtype='show_bandages',
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
                    subtype='show_tools',
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
