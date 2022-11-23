#!/usr/bin/env python3

import emails
import os
import reports
import datetime


def get_all_text_files(txt_dir):
    return [x for x in os.listdir(txt_dir) if x.endswith('.txt')]


def process_txt_name_weight(txt_file):
    file_lines = txt_file.readlines()
    json_dict = {}
    i = 0
    for line in file_lines:
        if i == 0:
            json_dict['name'] = line
        elif i == 1:
            json_dict['weight'] = int(line.split()[0])
        else:
            break
        i += 1

    return json_dict


def process_paragraph():
    txt_dir = 'supplier-data/descriptions/'
    txt_filenames = get_all_text_files(txt_dir)
    json_dict = []
    for filename in txt_filenames:
        with open(txt_dir + filename, 'r') as file:
            json_dict.append(process_txt_name_weight(file))
    return (json_dict)


if __name__ == "__main__":
    para_dict = process_paragraph()
    present_date = datetime.datetime.now().strftime("%B %d, %Y")
    report_title = 'Processed Update on ' + present_date
    print(report_title)
    reports.generate_report('processed.pdf', report_title, para_dict)

    sender = 'automation@example.com'
    # Replace username with the username given in the Connection Details Panel on the right hand side.
    username = 'student32'
    recipient = '{}@example.com'.format(username)
    subject = 'Upload Completed - Online Fruit Store'
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = '/tmp/processed.pdf'
    # This mail_pass is given to at the start of the lab
    mail_pass = ''
    message = emails.generate_email(
        sender, recipient, subject, body, attachment)
    emails.send_email(message, mail_pass)
