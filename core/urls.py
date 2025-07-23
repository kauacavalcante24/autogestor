from django.contrib import admin
from django.urls import include, path

from .views import InicialView

urlpatterns = [
    path('', include('user.urls')),
    path('home/', InicialView.as_view(), name='inicial'),
    path('clientes/', include('customer.urls')),
    path('veiculos/', include('vehicles.urls')),
    path('manutencoes/', include('maintenances.urls')),
    path('admin/', admin.site.urls),
]
