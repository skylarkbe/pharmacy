from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addPharmaceutical', views.addPharmaceutical, name='addPharmaceutical')
]
