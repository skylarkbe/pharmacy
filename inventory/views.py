from django.shortcuts import render
from django.http import HttpResponse

from .models import Medicine


def index(request):
    all_medicines = Medicine.objects.all()
    context = {'all_medicines': all_medicines, }
    return render(request, 'inventory/index.html', context)


def addPharmaceutical(request):
    return HttpResponse("Hello world, you're at the add pharmaceutical page")
