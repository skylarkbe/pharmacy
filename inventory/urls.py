from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.index, name='index'),
    path('toggleFilter', views.toggle_filter, name='toggleFilter'),
    path('openSyrup', views.open_syrup, name='openSyrup'),
    path('addStockUnit', views.add_stock_unit, name='addStockUnit'),
    path('removeStockUnit', views.remove_stock_unit, name='removeStockUnit'),
    path('addPharmaceutical', views.AddPharmaceuticalView.as_view(), name='addPharmaceutical'),
    path('addMedicine', views.AddMedicineView.as_view(), name='addMedicine'),
]
