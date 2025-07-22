from django.views import generic
from django.urls import reverse_lazy
from .models import Vehicle, Brand
from customer.models import Customer
from .forms import VehicleModelForm


class VehicleCreateView(generic.CreateView):
    model = Vehicle
    template_name = 'vehicle_create.html'
    form_class = VehicleModelForm
    success_url = reverse_lazy('inicial')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brands = Brand.objects.all()
        customers = Customer.objects.all()
        context['brands'] = brands
        context['customers'] = customers
        return context


class VehicleListView(generic.ListView):
    model = Vehicle
    template_name = 'vehicles.html'
    context_object_name = 'vehicles'
