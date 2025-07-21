from .models import Customer
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomerModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from vehicles.models import Vehicle


class CustomerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Customer
    template_name = 'customer_create.html'
    form_class = CustomerModelForm
    success_url = reverse_lazy('inicial')

class CustomerListView(LoginRequiredMixin, generic.ListView):
    model = Customer
    template_name = 'customers.html'
    context_object_name = 'customers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search')

        if search:
            customers_query = Customer.objects.filter(name__icontains=search).order_by('name')
        else:
            customers_query = Customer.objects.none()
        
        context['customers_query'] = customers_query
        context['search_query'] = search

        return context


class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Customer
    template_name = 'customer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle = Vehicle.objects.filter(owner_id=self.object.id)
        context['vehicle'] = vehicle
        return context
