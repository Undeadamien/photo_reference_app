import io

import requests

url = "https://api.scryfall.com/cards/random"
headers = {"Content-Type": "application/json"}


def request_image(amount):
    images = []

    while len(images) < amount:
        res = requests.get(url, headers=headers, timeout=30).json()

        try:
            image_url = res["image_uris"]["art_crop"]
            print(res["name"])
        except KeyError:
            continue

        image = requests.get(image_url, timeout=30).content
        images.append(io.BytesIO(image))

    return images
