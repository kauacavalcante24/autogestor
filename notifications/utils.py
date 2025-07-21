import os
from django.core.mail import send_mail
from datetime import datetime


def date_format():
    date = datetime.now().strftime('%d/%m/%Y')
    return date


def send_email_worker(user):
    date = date_format()
    email = os.getenv('EMAIL_HOST_USER')
    print('=' * 50)
    print(f'Automatic email was sent to {user.first_name}')
    print(f'Email: {user.email}')
    print('=' * 50)

    subject = 'AutoGestor - Boas-vindas!'
    html_message = f'''
        <h1>Olá {user.first_name},</h1>

        <p>Seja muito bem-vindo à equipe <strong>AutoGestor</strong>!</p>

        <p>Estamos felizes por contar com você em nosso time. Sua contribuição será fundamental para continuarmos oferecendo um serviço de qualidade e confiança aos nossos clientes.</p>
        <p>Caso tenha dúvidas sobre seu acesso ao sistema, horários ou procedimentos internos, estamos à disposição para ajudar. Contato: <strong>83 90000-8000</strong></p>
        <p>Mais uma vez, seja bem-vindo — e sucesso nessa nova jornada conosco!</p>

        <p>Nossa oficina agradece. Até logo!</p>

        <strong>Atenciosamente, AutoGestor – {date}.</strong>
    '''
    from_email = f'AutoGestor <{email}>'
    recipient_list = [user.email]

    try:
        send_mail(
            subject=subject,
            message='',
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False,
        )
    except:
        print('-' * 50)
        print(f'==> Falha ao enviar email para {user.first_name}')
        print(f'Endereço: {user.email}')
        print('-' * 50)


def send_email_customer(customer):
    date = date_format()
    email = os.getenv('EMAIL_HOST_USER')
    print('=' * 50)
    print(f'Automatic email was sent to {customer.name}')
    print(f'Email: {customer.email}')
    print('=' * 50)

    subject = 'AutoGestor - Boas-vindas!'
    html_message = f'''
        <h1>Olá {customer.name},</h1>

        <p>Seja muito bem-vindo à <strong>AutoGestor</strong>!</p>

        <p>É um prazer tê-lo como nosso cliente. Estamos comprometidos em oferecer um atendimento de qualidade, com transparência, agilidade e confiança para cuidar do seu veículo da melhor forma possível.</p>
        <p>Se tiver dúvidas sobre nossos serviços, agendamentos ou qualquer outra necessidade, nossa equipe está à disposição para ajudar. Entre em contato pelo WhatsApp: <strong>83 90000-8000</strong>.</p>

        <p>Obrigado por escolher a AutoGestor. Esperamos superar suas expectativas!</p>

        <strong>Atenciosamente,<br> AutoGestor – {date}.</strong>
    '''

    from_email = f'AutoGestor <{email}>'
    recipient_list = [customer.email]

    try:
        send_mail(
            subject=subject,
            message='',
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False,
        )
    except:
        print('-' * 50)
        print(f'==> Falha ao enviar email para {customer.first_name}')
        print(f'Endereço: {customer.email}')
        print('-' * 50)
