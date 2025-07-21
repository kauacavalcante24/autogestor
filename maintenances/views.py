from django.views import generic
from django.urls import reverse_lazy
from .models import Maintenances, Service
from django.contrib.auth.models import User
from vehicles.models import Vehicle
from .forms import MaintenancesModelForm


class MaintenanceListView(generic.ListView):
    model = Maintenances
    template_name = 'maintenances.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        maintenances = Maintenances.objects.all()
        context['maintenances'] = maintenances
        return context


class MaintenanceDetailView(generic.DetailView):
    model = Maintenances
    template_name = 'maintenance_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Service.objects.filter(maintenances=self.object.pk)
        context['services'] = services
        return context
    

class MaintenanceCreateView(generic.CreateView):
    model = Maintenances
    template_name = 'maintenance_create.html'
    form_class = MaintenancesModelForm
    success_url = reverse_lazy('maintenances_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicles = Vehicle.objects.all()
        workers = User.objects.all()
        context['vehicles'] = vehicles
        context['workers'] = workers
        return context