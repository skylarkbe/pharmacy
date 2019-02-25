from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.index, name='index'),
    path('toggleFilter', views.toggle_filter, name='toggleFilter'),
    path('openSyrup', views.open_syrup, name='openSyrup'),
    path('addPharmaceutical', views.AddPharmaceuticalView.as_view(), name='addPharmaceutical'),
    path('addMedicine', views.AddMedicineView.as_view(), name='addMedicine'),
]
