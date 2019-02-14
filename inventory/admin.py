from django.contrib import admin

from .models import *


class PharmaceuticalAdmin(admin.ModelAdmin):
    model = Pharmaceutical
    list_display = ('id', 'name', 'medicalPrescription')


class MedicineAdmin(admin.ModelAdmin):
    readonly_fields = ('insertDate',)


admin.site.site_header = "MyPharmacy Admin"
admin.site.site_title = "MyPharmacy Admin Portal"
admin.site.index_title = "Welcome to MyPharmacy Admin Portal"
admin.site.register(Pharmaceutical, PharmaceuticalAdmin)
admin.site.register(Pill,MedicineAdmin)
admin.site.register(Syrup,MedicineAdmin)
