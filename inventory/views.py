from django.shortcuts import render

from .models import Medicine


def index(request):
    all_medicines = Medicine.objects.all()
    context = {'all_medicines': all_medicines, }
    return render(request, 'inventory/index.html', context)
