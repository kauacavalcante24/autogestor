from django.db import models

from customer.models import Customer


class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome', unique=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    owner = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='owner',
        verbose_name='Proprietário'
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name='brand',
        verbose_name='Marca'
    )
    model = models.CharField(max_length=100, verbose_name='Modelo')
    plate = models.CharField(max_length=20, verbose_name='Placa', unique=True)
    year = models.IntegerField(verbose_name='Ano')
    color = models.CharField(max_length=50, verbose_name='Cor')
    created_at = models.DateTimeField(verbose_name='Entrada em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return f'{self.brand} {self.model} | {self.plate}'
