from django.urls import path

from .views import CustomerCreateView, CustomerDetailView, CustomerListView

urlpatterns = [
    path('', CustomerListView.as_view(), name='customers_list'),
    path('novo/', CustomerCreateView.as_view(), name='customer_create'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
]
