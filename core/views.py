from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import now
from django.views.generic import TemplateView

from customer.models import Customer
from maintenances.models import Maintenances


class InicialView(LoginRequiredMixin, TemplateView):
    template_name = 'inicial.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search = self.request.GET.get('search')
        if search:
            customers = Customer.objects.filter(name__icontains=search).order_by('name')
        else:
            customers = Customer.objects.none()

        context['customers'] = customers
        context['search_query'] = search
        context['now'] = now()
        context['objects_in_progress'] = (
            Maintenances.objects
            .filter(status='in_progress')
            .select_related('vehicle')
        )

        return context
