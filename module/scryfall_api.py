import io

import requests

API_URL = "https://api.scryfall.com/cards/random"
HEADERS = {"Content-Type": "application/json"}


def request_image(amount):
    images = []

    while len(images) < amount:
        response = requests.get(API_URL, headers=HEADERS, timeout=30)

        try:
            image_src = response.json()["image_uris"]["art_crop"]
            image = requests.get(image_src, timeout=30).content
            images.append(io.BytesIO(image))

        except KeyError:  # art_crop can be missing
            continue

    return images
