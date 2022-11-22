#!/usr/bin/env python3

import os
import requests


def get_all_text_files(txt_dir):
    return [x for x in os.listdir(txt_dir) if x.endswith('.txt')]


def process_txt(txt_file, filename):
    file_lines = txt_file.readlines()
    json_dict = {}
    i = 0
    for line in file_lines:
        if i == 0:
            json_dict['name'] = line
        elif i == 1:
            json_dict['weight'] = int(line.split()[0])
        elif i == 2:
            json_dict['description'] = line
        i += 1

    image_filename = filename.strip('.txt') + '.jpeg'
    json_dict['image_name'] = image_filename

    return json_dict


def post_txt(url):
    txt_dir = 'supplier-data/descriptions/'
    txt_filenames = get_all_text_files(txt_dir)
    for filename in txt_filenames:
        with open(txt_dir + filename, 'r') as file:
            json_val = process_txt(file, filename)
            print(json_val)
            requests.post(url, json=json_val)


url = 'http://localhost/fruits/'
post_txt(url)
