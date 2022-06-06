import os
import random

from PIL import Image


def create_image(images: list, file_name='Squad.png'):
    total = None
    for image in images:
        if total is None:
            total = Image.open(image)
        else:
            total = Image.alpha_composite(total, Image.open(image))
    total.save(file_name)


def grab_random_image(path: str):
    if path[-1] != '/':
        raise ValueError
    files = os.listdir(path)
    return f'{path}{random.choice(files)}'
