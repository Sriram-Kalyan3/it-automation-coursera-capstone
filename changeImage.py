#!/usr/bin/env python3
from PIL import Image
import os


def get_all_image_files(image_dir):
    pwd = os.getcwd() + image_dir
    # print(pwd)
    return [x for x in os.listdir(pwd) if x.endswith('.tiff')]


def modify_images():
    image_dir = '\supplier-data\images'
    images = get_all_image_files(image_dir)

    image_dir = 'supplier-data/images/'
    # print(image_dir)
    for image in images:
        save_path = os.path.join(image_dir, image.strip('.tiff'))
        im = Image.open(image_dir + image)
        resized_im = im.resize((600, 400))
        resized_im = resized_im.convert('RGB')
        resized_im.save(save_path.lstrip('[/\\]') + '.jpeg')

        os.remove(image_dir + image)


modify_images()
# print(get_all_image_files(image_dir))
