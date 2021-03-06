from django.contrib import admin

from .models import *


@admin.register(Pharmaceutical)
class PharmaceuticalAdmin(admin.ModelAdmin):
    model = Pharmaceutical
    list_display = ('id', 'name', 'medicalPrescription')
    list_filter = ('medicalPrescription',)


@admin.register(Pill)
class PillAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'expirationDate', 'is_medicine_expired',)
    readonly_fields = ('insertDate', 'is_expired','subtype',)


@admin.register(Syrup)
class SyrupAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'expirationDate', 'openedDate', 'validity', 'is_medicine_expired',)
    readonly_fields = ('insertDate', 'is_expired','subtype',)

@admin.register(Bandage)
class BandageAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'expirationDate', 'is_medicine_expired','openedDate',)
    readonly_fields = ('insertDate', 'is_expired','subtype',)

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'expirationDate', 'is_medicine_expired','is_sterile','openedDate',)
    readonly_fields = ('insertDate', 'is_expired','subtype',)

admin.site.site_header = "MyPharmacy Admin"
admin.site.site_title = "MyPharmacy Admin Portal"
admin.site.index_title = "Welcome to MyPharmacy Admin Portal"
