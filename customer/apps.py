from django.apps import AppConfig


class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'
    verbose_name = 'Cliente'

    # Para ativar o envio de email automático

    # def ready(self):
    #     import customer.signals
