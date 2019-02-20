from django.shortcuts import render
from django.http import HttpResponse

from .models import Medicine


def index(request):
    all_stock = Medicine.objects.all().select_subclasses()
    context = {'all_stock': all_stock, }
    return render(request, 'inventory/index.html', context)


def addPharmaceutical(request):
    return HttpResponse("Hello world, you're at the add pharmaceutical page")
