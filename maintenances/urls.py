from django.urls import path
from .views import MaintenanceListView, MaintenanceDetailView, MaintenanceCreateView


urlpatterns = [
    path('manutencao/', MaintenanceListView.as_view(), name='maintenances_list'),
    path('manutencao/<int:pk>', MaintenanceDetailView.as_view(), name='maintenance_detail'),
    path('manutencao/adicionar-manutencao/', MaintenanceCreateView.as_view(), name='maintenance_create'),
]