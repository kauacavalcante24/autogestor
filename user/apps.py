from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
    verbose_name = 'Funcionários'

    # Para ativar o envio de email automático

    # def ready(self):
    #     import user.signals
