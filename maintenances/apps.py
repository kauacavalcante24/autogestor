from django.apps import AppConfig


class MaintenancesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'maintenances'
    verbose_name = 'Manutenção'

    def ready(self):
        import maintenances.signals
