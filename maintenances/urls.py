from django.urls import path

from .views import (MaintenanceCreateView, MaintenanceDetailView,
                    MaintenanceListView)

urlpatterns = [
    path('', MaintenanceListView.as_view(), name='maintenances_list'),
    path('<int:pk>/', MaintenanceDetailView.as_view(), name='maintenance_detail'),
    path('novo/', MaintenanceCreateView.as_view(), name='maintenance_create'),
]
