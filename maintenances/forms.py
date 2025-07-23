from django import forms

from .models import Maintenances


class MaintenancesModelForm(forms.ModelForm):

    class Meta:
        model = Maintenances
        fields = ['vehicle', 'description', 'total_value', 'exit_date', 'status', 'responsible']

    def clean(self):
        cleaned_data = super().clean()
        vehicle = cleaned_data.get('vehicle')

        if vehicle:
            has_active = Maintenances.objects.filter(
                vehicle=vehicle,
                status='in_progress'
            ).exists()

            if has_active:
                raise forms.ValidationError(
                    f'{vehicle.brand} {vehicle.model} de placa {vehicle.plate} já está em manutenção (status: Em andamento).'
                )

            is_waiting = Maintenances.objects.filter(
                vehicle=vehicle,
                status='waiting'
            )

            if is_waiting:
                raise forms.ValidationError(
                    f'{vehicle.brand} {vehicle.model} de placa {vehicle.plate} já está em manutenção (status: Aguardando aprovação)'
                )

        return cleaned_data
