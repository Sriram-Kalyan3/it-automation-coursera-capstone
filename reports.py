#!/usr/bin/env python3

from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
import os


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


def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment + '.pdf')
    styles = getSampleStyleSheet()

    report_title = Paragraph(title, styles["h1"])
    txt_dir = 'supplier-data/descriptions/'
    txt_filenames = get_all_text_files(txt_dir)
    json_dict = []
    report_paragraph = []
    '''
    report_paragraph = ["name: Strawberry<br/>weight: 300 lbs<br/><br/>", ""....]
    '''
    for filename in txt_filenames:
        with open(txt_dir + filename, 'r') as file:
            json_dict.append(process_txt_name_weight(file))
    for item in json_dict:
        short_para = "name: {}<br/>weight: {} lbs<br/><br/>".format(
            item["name"], item["weight"]).replace('\n', '')
        short_para = Paragraph(short_para)
        report_paragraph.append(short_para)
    report.build([report_title] + report_paragraph)


# generate_report('test', 'Just checking', 'asdf')
