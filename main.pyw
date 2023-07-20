import ast
import configparser
import io
import pathlib
import random

import requests

from module.reference_window import ReferenceWindow
from module.setup_window import SetupWindow

config = configparser.ConfigParser()
config.read(pathlib.Path(__file__).parent / "config.ini")

API_URL = "https://api.scryfall.com/cards/random"
DEFAULT_AMOUNT = int(config.get("Settings", "Default_amount", fallback="4"))
DEFAULT_TIME = int(config.get("Settings", "Default_time", fallback="5"))
IMAGE_PATH = pathlib.Path(config.get("Settings", "Path"))
LOCAL = config.getboolean("Settings", "Local", fallback=True)
MAX_IMAGE = int(config.get("Settings", "Max_image", fallback="10"))
ONLINE = config.getboolean("Settings", "Online", fallback=False)
DIR_SIZE = len(list(IMAGE_PATH.glob("*.jpg")))
POS = ast.literal_eval(config.get("Settings", "Position", fallback="(0, 40)"))
SIZE = ast.literal_eval(config.get("Settings", "Size", fallback="(400, 400)"))


def request_image(url: str, amount: int):
    images = set()
    while len(images) < amount:
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            image_src = response.json()["image_uris"]["art_crop"]
            image = requests.get(image_src, timeout=30).content
            images.add(io.BytesIO(image))
        except (requests.RequestException, KeyError):
            continue
    return list(images)


def sample_image(amount: int, path: pathlib.Path) -> list[io.BytesIO]:
    sampled_images = set()
    while len(sampled_images) < amount:
        image_file = random.choice(list(path.glob("*.jpg")))
        try:
            with image_file.open(mode="rb") as file:
                sampled_images.add(io.BytesIO(file.read()))
        except PermissionError:
            continue
    return list(sampled_images)


def run_application():
    assert ONLINE or LOCAL, "ONLINE or LOCAL must be set to true"

    set_win = SetupWindow(DIR_SIZE, DEFAULT_TIME, DEFAULT_AMOUNT)
    time, amount = set_win.run()

    if time and amount:
        if ONLINE:
            images = request_image(API_URL, amount)
        elif LOCAL:
            images = sample_image(amount, IMAGE_PATH)

    ref_win = ReferenceWindow(time, images, POS, SIZE)
    ref_win.run()


if __name__ == "__main__":
    run_application()
