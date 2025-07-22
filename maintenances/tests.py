from django.test import TestCase
from django.urls import reverse
from .models import Maintenances
from vehicles.models import Vehicle, Brand
from customer.models import Customer
from django.contrib.auth.models import User


class MaintenancesTestView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='kaua', password='kaua123321')
        self.owner = Customer.objects.create(name='Kauã Silva', phone_number='21987675464')
        self.brand = Brand.objects.create(name='Chevrolet')
        self.vehicle = Vehicle.objects.create(
            owner=self.owner,
            brand=self.brand,
            model='Civic',
            plate='HFJ6J89',
            year=2010,
            color='Amarelo'
        )
        Maintenances.objects.create(
            vehicle=self.vehicle,
            status='waiting',
            responsible=self.user
        )

    def test_maintenance_list_view(self):
        self.client.login(username='kaua', password='kaua123321')
        response = self.client.get(reverse('maintenances_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maintenances.html')
        self.assertContains(response, 'Civic')
        self.assertContains(response, 'HFJ6J89')
