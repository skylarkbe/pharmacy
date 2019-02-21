from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _trans

from .models import Medicine, Pharmaceutical
from .forms import AddPharmaceuticalForm


def index(request):
    all_stock = Medicine.objects.all().select_subclasses()
    return render(request, 'inventory/index.html', {'all_stock': all_stock})


class AddPharmaceuticalView(TemplateView):
    template_name = "inventory/addPharmaceutical.html"

    def get(self, request, *args, **kwargs):
        add_pharmaceutical = AddPharmaceuticalForm()
        return render(request, 'inventory/addPharmaceutical.html', {'add_pharmaceutical_form': add_pharmaceutical})

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
            return render(request, 'inventory/addPharmaceutical.html', {'add_pharmaceutical_form': add_pharmaceutical})
