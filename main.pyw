import io
import json
import pathlib
import random

import requests

from module.reference_window import ReferenceWindow
from module.setup_window import SetupWindow

CONFIG_FILE = pathlib.Path(__file__).parent / "config.json"


def load_config(config_file: str | pathlib.Path) -> dict:
    with config_file.open() as config:
        return json.load(config)


def request_image(url: str, amount: int) -> list[io.BytesIO]:
    images = set()
    while len(images) < amount:
        try:
            card_response = requests.get(url, timeout=30)
            image_src = card_response.json()["image_uris"]["art_crop"]
            image_response = requests.get(image_src, timeout=30)
            image = image_response.content
            images.add(io.BytesIO(image))

        except (requests.RequestException, KeyError):
            continue

    return list(images)


def sample_image(amount: int, path: pathlib.Path) -> list[io.BytesIO]:
    sampled_images = set()
    while len(sampled_images) < amount:
        try:
            image_file = random.choice(list(path.glob("*.jpg")))
            with image_file.open(mode="rb") as file:
                sampled_images.add(io.BytesIO(file.read()))
        except PermissionError:
            continue

    return list(sampled_images)


def main():
    config = load_config(CONFIG_FILE)
    DEFAULT_AMOUNT = config["default"]["amount"]
    DEFAULT_TIME = config["default"]["time"]
    IMAGE_PATH = pathlib.Path(config["path"])
    POSITION = config["position"]
    ONLINE = config["online"]
    SIZE = config["size"]
    API_URL = config["api_url"]
    MAX_IMAGE = len(list(pathlib.Path(config["path"]).glob("*.jpg")))

    set_win = SetupWindow(MAX_IMAGE, DEFAULT_TIME, DEFAULT_AMOUNT)
    time, amount = set_win.run()
    if not (time and amount):
        return

    if ONLINE:
        images = request_image(API_URL, amount)
    else:
        images = sample_image(amount, IMAGE_PATH)

    ref_win = ReferenceWindow(time, images, POSITION, SIZE)
    ref_win.run()


if __name__ == "__main__":
    main()
