from django.contrib import admin
from django.urls import include, path

from .views import InicialView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicialView.as_view(), name='inicial'),
    path('clientes/', include('customer.urls')),
    path('veiculos/', include('vehicles.urls')),
    path('manutencoes/', include('maintenances.urls')),
    path('usuarios/', include('user.urls')),

]
