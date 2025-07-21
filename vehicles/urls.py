from django.urls import path
from .views import VehicleCreateView


urlpatterns = [
    path('veiculo/adicionar/', VehicleCreateView.as_view(), name='vehicle_create')
]