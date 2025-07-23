from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Customer


class CustomerViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='kaua', password='kaua123321')
        Customer.objects.create(name='Kauã Silva', phone_number='21987675464')

    def test_customer_list_view(self):
        self.client.login(username='kaua', password='kaua123321')
        response = self.client.get(reverse('customers_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers.html')
        self.assertContains(response, 'Kauã Silva')
