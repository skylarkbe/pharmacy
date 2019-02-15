from django.shortcuts import render

from .models import Syrup


def index(request):
    all_medicines = Syrup.objects.all()
    context = {'all_medicines': all_medicines, }
    return render(request, 'inventory/index.html', context)
