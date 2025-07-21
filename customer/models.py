from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    phone_number = models.CharField(verbose_name='Telefone')
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    cpf = models.CharField(verbose_name='CPF', null=True, blank=True, unique=True)
    created_at = models.DateTimeField(verbose_name='Entrada em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name
