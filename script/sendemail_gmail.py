# coding: utf-8

import email.message
import smtplib
from os import system

system('clear')


def enviar_email():
    corpo_email = """
    <p>Olá, Jefersom</p>
    <p>Segue email conforme solicitado...</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'heimdallcodebr@gmail.com'
    msg['To'] = 'heimdallcodebr@gmail.com'
    password = 'password_app'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


enviar_email()
