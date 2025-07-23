from django.test import TestCase
from django.urls import reverse

from customer.models import Customer

from .models import Brand, Vehicle


class VehicleTestView(TestCase):

    def setUp(self):
        self.owner = Customer.objects.create(name='Kauã Silva', phone_number='21987675464')
        self.brand = Brand.objects.create(name='Chevrolet')
        Vehicle.objects.create(
            owner=self.owner,
            brand=self.brand,
            model='Civic',
            plate='HFJ6J89',
            year=2010,
            color='Amarelo'
        )

    def test_vehicle_list_view(self):
        response = self.client.get(reverse('vehicles_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vehicles.html')
        self.assertContains(response, 'Civic')
        self.assertContains(response, 'HFJ6J89')
        self.assertContains(response, 2010)
        self.assertContains(response, 'Amarelo')
