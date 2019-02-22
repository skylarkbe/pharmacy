from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.index, name='index'),
    path('addPharmaceutical', views.AddPharmaceuticalView.as_view(), name='addPharmaceutical'),
    path('addMedicine', views.AddMedicineView.as_view(), name='addMedicine'),
]
