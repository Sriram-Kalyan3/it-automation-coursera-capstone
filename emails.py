#!/usr/bin/env python3

import smtplib
from email.message import EmailMessage
import os.path
import mimetypes


def generate_email(sender, recipient, subject, body, attachment):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=os.path.basename(attachment))
    return message


def generate_email_without_attachment(sender, recipient, subject, body):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    return message


def send_email(message, mail_pass):
    mail_server = smtplib.SMTP_SSL('smtp.example.com')
    mail_server.set_debuglevel(1)
    mail_server.login(message['From'], mail_pass)
    mail_server.send_message(message)
    mail_server.quit()
