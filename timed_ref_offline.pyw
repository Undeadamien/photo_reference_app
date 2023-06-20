import io
from pathlib import Path
from random import sample

from module.reference_window import ReferenceWindow
from module.setup_window import SetupWindow

IMAGE_PATH = Path("C:/Users/Damien/Drawing/Photo_ref")


def sample_image(amount: int) -> list[io.BytesIO]:
    sampled_images = []

    try:
        image_files = sample(list(IMAGE_PATH.glob("*.jpg")), amount)
        for image in image_files:
            with image.open(mode="rb") as file:
                sampled_images.append(io.BytesIO(file.read()))

    except PermissionError as e:
        print("Error occurred while reading image files:", str(e))

    return sampled_images


def run_application():
    if not IMAGE_PATH.exists() or not IMAGE_PATH.is_dir():
        return
    if len(list(IMAGE_PATH.glob("*.jpg"))) <= 0:
        return

    time_and_amount = []

    file_quantity = len(list(IMAGE_PATH.glob("*.jpg")))
    SetupWindow(time_and_amount, file_quantity).run()

    selected_image = sample_image(time_and_amount[1])
    ReferenceWindow(time_and_amount[0], selected_image).run()


if __name__ == "__main__":
    run_application()
