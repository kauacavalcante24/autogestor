from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from notifications.utils import send_email_worker


@receiver(post_save, sender=User)
def send_email(sender, instance, created, **kwargs):
    if created and instance.email:
        try:
            send_email_worker(instance)
            print('==> EMAIL ENVIADO')
        except:
            print('-' * 50)
            print(f'==> Falha ao enviar email para {instance.first_name}')
            print(f'Endereço: {instance.email}')
            print('-' * 50)
