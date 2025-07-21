from django.db import models
from vehicles.models import Vehicle
from django.contrib.auth.models import User


STATUS_MAINTENANCES = (
    ('waiting', 'Aguardando aprovação'),
    ('in_progress', 'Em andamento'),
    ('completed', 'Concluído'),
)

class ServiceType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nome do Serviço')

    class Meta:
        verbose_name = 'Tipo de Serviço'
        verbose_name_plural = 'Tipos de Serviços'

    def __str__(self):
        return self.name


class Maintenances(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        related_name='vehicle_maintenances',
        on_delete=models.PROTECT,
        verbose_name='Veículo'
    )
    description = models.TextField(max_length=500, verbose_name='Descrição', null=True, blank=True)
    total_value = models.DecimalField(
        default=0,
        verbose_name='Valor Total',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    entry_date = models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')
    exit_date = models.DateTimeField(null=True, blank=True, verbose_name='Data de Saída')
    status = models.CharField(
        max_length=100,
        choices=STATUS_MAINTENANCES,
        verbose_name='Status'
    )
    responsible = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='user_maintenances',
        verbose_name='Responsável'
    )

    class Meta:
        verbose_name = 'Manutenção'
        verbose_name_plural = 'Manutenções'
    
    def __str__(self):
        return f'{self.vehicle.brand} {self.vehicle.model} | {self.vehicle.plate}'


class Service(models.Model):
    maintenances = models.ForeignKey(
        Maintenances,
        on_delete=models.CASCADE,
        related_name='services',
        verbose_name='Manutenção'
    )
    service_type = models.ForeignKey(
        ServiceType,
        on_delete=models.PROTECT,
        related_name='services_type',
        verbose_name='Tipo de Serviço'
    )
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return f'{self.service_type} | R${self.value}'
