from django import forms
from django.utils.timezone import now

from .models import Vehicle


class VehicleModelForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = ['owner', 'brand', 'model', 'year', 'plate', 'color']
        widgets = {
            'model': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'plate': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year < 1000 or year > now().year:
            raise forms.ValidationError('O ano informado é inválido! Tente Novamente.')
        return year

    def clean_model(self):
        model = self.cleaned_data.get('model')
        return model.capitalize()

    def clean_color(self):
        color = self.cleaned_data.get('color')
        return color.capitalize()
