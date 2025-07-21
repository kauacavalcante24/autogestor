from django.contrib import admin
from .models import ServiceType, Maintenances, Service
from vehicles.models import Vehicle


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(Maintenances)
class MaintenancesAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'description', 'total_value', 'entry_date', 'exit_date', 'status', 'responsible']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'vehicle':
            used = Maintenances.objects.filter(status='in_progress').values_list('vehicle_id', flat=True)
            kwargs["queryset"] = Vehicle.objects.exclude(id__in=used)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['maintenances', 'service_type', 'value']
