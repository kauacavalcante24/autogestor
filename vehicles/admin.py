from django.contrib import admin
from .models import Brand, Vehicle


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['owner', 'brand', 'model', 'plate', 'year', 'color']
