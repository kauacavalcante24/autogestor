from django.urls import path

from .views import VehicleCreateView, VehicleListView

urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicles_list'),
    path('novo/', VehicleCreateView.as_view(), name='vehicle_create'),
]
