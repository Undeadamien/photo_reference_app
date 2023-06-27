import io

import requests

from module.reference_window import ReferenceWindow
from module.setup_window import SetupWindow

API_URL: str = "https://api.scryfall.com/cards/random"
ARGUMENTS: dict[str, list[str]] = {
    "type": ["Land", "Creature"],
    "artist": ["John Avon", "Magali Villeneuve"],
}


def add_arguments(url: str, arguments: dict[str, list[str]]):
    if not arguments:
        return url

    url += "?q="
    for argument, values in arguments.items():
        parsed = [f"{argument}%3A{value.replace(' ', '')}" for value in values]
        url += f"%28{'+or+'.join(parsed)}%29"
    return url


def request_image(url: str, amount: int):
    images = set()

    while len(images) < amount:
        response = requests.get(url, timeout=30)

        try:
            image_src = response.json()["image_uris"]["art_crop"]
            image = requests.get(image_src, timeout=30).content
            images.add(io.BytesIO(image))
        except KeyError:  # art_crop can be missing
            continue

    return list(images)


def run_application():
    url = add_arguments(API_URL, ARGUMENTS)

    time, amount = SetupWindow().run()
    ReferenceWindow(time, request_image(url, amount)).run()


if __name__ == "__main__":
    run_application()
