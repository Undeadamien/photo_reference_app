import io

import requests

from module.reference_window import ReferenceWindow
from module.setup_window import SetupWindow

API_URL = "https://api.scryfall.com/cards/random"
HEADERS = {"Content-Type": "application/json"}


def request_image(amount: int, url: str, headers: dict):
    images = []
    while len(images) < amount:
        response = requests.get(url, headers=headers, timeout=30)
        try:
            image_src = response.json()["image_uris"]["art_crop"]
            image = requests.get(image_src, timeout=30).content
            images.append(io.BytesIO(image))
        except KeyError:  # art_crop can be missing
            continue

    return images


def run_application():
    time, amount = SetupWindow().run()
    ReferenceWindow(time, request_image(amount, API_URL, HEADERS)).run()


if __name__ == "__main__":
    run_application()
