from django import forms

from .models import Customer


class CustomerModelForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'phone_number', 'email', 'cpf']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Ex: (00) 98888-7777',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ex: usuario@email.com',
                'class': 'form-control'
            }),
            'cpf': forms.NumberInput(attrs={
                'placeholder': 'Apenas números',
                'class': 'form-control'
            })
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if any(num.isalpha() for num in phone_number):
            raise forms.ValidationError("O telefone não pode conter letras.")
        return phone_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name.title()
