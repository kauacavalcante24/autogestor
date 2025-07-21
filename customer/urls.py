from django.urls import path
from .views import CustomerCreateView, CustomerListView, CustomerDetailView


urlpatterns = [
    path('clientes/', CustomerListView.as_view(), name='customers_list'),
    path('clientes/adicionar-cliente/', CustomerCreateView.as_view(), name='customer_create'),
    path('clientes/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
]