from PIL import Image


def create_image(images: list, file_name='Squad.png'):
    total = None
    for image in images:
        if total is None:
            total = Image.open(image)
        else:
            total = Image.alpha_composite(total, Image.open(image))
    total.save(file_name)
