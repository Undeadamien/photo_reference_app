import io
import json
import pathlib
import random
import sys

import requests

from module.reference_window import ReferenceWindow
from module.setup_window import SetupWindow

CONFIG_FILE: pathlib.Path = pathlib.Path(__file__).parent / "config.json"
with CONFIG_FILE.open() as config:
    config = json.load(config)
# setup window parameters
DEFAULT_AMOUNT: int = config["default"]["amount"]
DEFAULT_TIME: int = config["default"]["time"]
MAX_IMAGE: int = len(list(pathlib.Path(config["path"]).glob("*.jpg")))
# reference window parameters
POSITION: tuple[int, int] = config["position"]
SIZE: tuple[int, int] = config["size"]
# image source
PATH: pathlib.Path = pathlib.Path(config["path"])
ONLINE: bool = config["online"]
QUERY: str = config["query"]
API_URL: str = config["api_url"]
URL: str = f"{API_URL}?q={QUERY}" if QUERY else API_URL


def request(url: str, amount: int) -> list[io.BytesIO]:
    images = set()

    while len(images) < amount:
        try:
            # request a random card from the api
            card_response = requests.get(url, timeout=30)
            card_response.raise_for_status()
            image_src = card_response.json()["image_uris"]["art_crop"]
            # retrieve the art of this image
            image_response = requests.get(image_src, timeout=30)
            image_response.raise_for_status()
            images.add(io.BytesIO(image_response.content))

        except KeyError:  # probably no art crop
            continue
        except requests.HTTPError:  # probably no connection
            raise requests.HTTPError

    return list(images)


def sample(path: str, amount: int) -> list[io.BytesIO]:
    sampled_images = set()

    while len(sampled_images) < amount:
        try:
            image_file = random.choice(list(path.glob("*.jpg")))
            with image_file.open(mode="rb") as file:
                sampled_images.add(io.BytesIO(file.read()))

        except PermissionError:  # the file is probably open
            continue

    return list(sampled_images)


def main() -> None:
    setup_window = SetupWindow(DEFAULT_TIME, DEFAULT_AMOUNT, MAX_IMAGE)
    time, amount = setup_window.run()

    if not (time and amount):
        sys.exit()

    images = request(URL, amount) if ONLINE else sample(PATH, amount)

    reference_window = ReferenceWindow(time, images, POSITION, SIZE)
    reference_window.run()


if __name__ == "__main__":
    main()
