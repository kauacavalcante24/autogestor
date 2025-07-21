from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Service

def update_maintenance_total(maintenance):
    services = maintenance.services.all()
    total = 0 
    for service in services:
        total += service.value

    maintenance.total_value = total
    maintenance.save(update_fields=['total_value'])

@receiver(post_save, sender=Service)
def update_total_on_service_save(sender, instance, **kwargs):
    update_maintenance_total(instance.maintenances)

@receiver(post_delete, sender=Service)
def update_total_on_service_delete(sender, instance, **kwargs):
    update_maintenance_total(instance.maintenances)
