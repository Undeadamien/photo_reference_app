import io
from os import listdir
from os.path import join
from random import sample

from module.reference_window import ReferenceWindow
from module.setup_window import SetupWindow

PATH = r"C:\Users\Damien\Drawing\Photo_ref"
images = [join(PATH, file) for file in listdir(PATH) if file.endswith(".jpg")]


def sample_image(amount: int) -> list[io.BytesIO]:
    sampled_images = []
    for image in sample(images, amount):
        with open(image, mode="rb") as data:
            sampled_images.append(io.BytesIO(data.read()))
    return sampled_images


def main():
    mediator = []  # [time, amount]
    SetupWindow(mediator, len(images)).run()
    ReferenceWindow(mediator[0], sample_image(mediator[1])).run()


if __name__ == "__main__":
    main()
