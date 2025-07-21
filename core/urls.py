from django.contrib import admin
from django.urls import path, include
from .views import InicialView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicialView.as_view(), name='inicial'),
    path('', include('customer.urls'), name='customers'),
    path('', include('vehicles.urls'), name='vehicles'),
    path('', include('maintenances.urls'), name='maintenances'),
    path('', include('user.urls'), name='users'),
]
