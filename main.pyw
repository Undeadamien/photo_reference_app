import io
import json
import pathlib
import random

import requests

from module.reference_window import ReferenceWindow
from module.setup_window import SetupWindow

CONFIG_FILE: pathlib.Path = pathlib.Path(__file__).parent / "config.json"
with CONFIG_FILE.open() as config:
    config = json.load(config)
DEFAULT_AMOUNT: int = config["default"]["amount"]
DEFAULT_TIME: int = config["default"]["time"]
IMAGE_PATH: pathlib.Path = pathlib.Path(config["path"])
POSITION: tuple[int, int] = config["position"]
ONLINE: bool = config["online"]
SIZE: tuple[int, int] = config["size"]
API_URL: str = config["api_url"]
MAX_IMAGE: int = len(list(pathlib.Path(config["path"]).glob("*.jpg")))
QUERY: dict[str, list[str]] = config["query"]


def request_image(url: str, amount: int) -> list[io.BytesIO]:
    images = set()
    if QUERY:
        url += f"?q={QUERY}"

    while len(images) < amount:
        try:
            card_response = requests.get(url, timeout=30)
            card_response.raise_for_status()
            json_response = card_response.json()
            image_src = json_response["image_uris"]["art_crop"]
            image_response = requests.get(image_src, timeout=30)
            image = image_response.content
            images.add(io.BytesIO(image))

        except KeyError:
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
