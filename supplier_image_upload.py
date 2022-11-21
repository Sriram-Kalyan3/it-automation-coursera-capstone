#!/usr/bin/env python3

import requests
import os


def get_all_jpeg_files(image_dir):
    pwd = os.getcwd() + '/' + image_dir
    return [x for x in os.listdir(pwd) if x.endswith('.jpeg')]


def upload(url):
    image_dir = 'supplier-data/images/'
    images = get_all_jpeg_files(image_dir)
    for image in images:
        with open(image_dir + image, 'rb') as image_file:
            r = requests.post(url, files={'file': image_file})


url = 'http://localhost/upload/'
upload(url)
