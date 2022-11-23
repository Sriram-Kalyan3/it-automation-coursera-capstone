#!/usr/bin/env python3

import socket
import psutil
import shutil
import emails
import os


def check_cpu():
    cpu_usage = psutil.cpu_percent()
    return cpu_usage > 80


def check_disk():
    available_disk = shutil.disk_usage('/')
    return available_disk[2] < 20


def check_memory():
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory < 500


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost != '127.0.0.1'


def run_tests(checks):
    error_msg = None
    for action, msg in checks.items():
        if action:
            error_msg = msg
    # send email
    if error_msg:
        sender = 'automation@example.com'
        recipient = '{}@example.com'.format(os.environ.get('USER'))
        subject = error_msg
        body = 'Please check your system and resolve the issue as soon as possible.'
        # Mail pass is given the connection details
        mail_pass = ''
        message = emails.generate_email_without_attachment(
            sender, recipient, subject, body)

        emails.send_email(message, mail_pass)


checks = {check_cpu(): "Error - CPU usage is over 80%",
          check_disk(): "Error - Available disk space is less than 20%",
          check_memory(): "Error - Available memory is less than 500MB",
          check_localhost(): "Error - localhost cannot be resolved to 127.0.0.1"}

run_tests(checks)
