import io
import pathlib
import random

from module.reference_window import ReferenceWindow
from module.setup_window import SetupWindow

IMAGE_PATH = pathlib.Path("C:/Users/Damien/Drawing/Photo_ref")


def sample_image(amount: int, path: pathlib.Path, extension: str) -> list[io.BytesIO]:
    image_files = random.sample(list(path.glob(f"*.{extension}")), amount)
    sampled_images = []

    for image in image_files:
        try:
            with image.open(mode="rb") as file:
                sampled_images.append(io.BytesIO(file.read()))
        except PermissionError as exception:
            print(exception)

    return sampled_images


def run_application():
    file_quantity = len(list(IMAGE_PATH.glob("*.jpg")))
    time, amount = SetupWindow(file_quantity).run()

    if time and amount:
        selected_image = sample_image(amount, IMAGE_PATH, "jpg")
        ReferenceWindow(time, selected_image).run()


if __name__ == "__main__":
    run_application()
