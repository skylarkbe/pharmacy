from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.index, name='index'),
    path('toggleFilter', views.toggle_filter, name='toggleFilter'),
    path('openSyrup', views.open_syrup, name='openSyrup'),
    path('addStockUnit', views.add_stock_unit, name='addStockUnit'),
    path('removeStockUnit', views.remove_stock_unit, name='removeStockUnit'),
    path('addPharmaceutical',login_required(views.AddPharmaceuticalView.as_view()), name='addPharmaceutical'),
    path('addMedicine', login_required(views.AddMedicineView.as_view()), name='addMedicine'),
    path('login', auth_views.LoginView.as_view()),
    path('logout', auth_views.LogoutView.as_view()),
]
