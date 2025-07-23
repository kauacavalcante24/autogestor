from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.utils import send_email_customer

from .models import Customer


@receiver(post_save, sender=Customer)
def send_email(sender, instance, created, **kwargs):
    if created and instance.email:
        try:
            send_email_customer(instance)
            print('==> EMAIL ENVIADO')
        except:
            print('-' * 50)
            print(f'==> Falha ao enviar email para {instance.name}')
            print(f'Endereço: {instance.email}')
            print('-' * 50)
