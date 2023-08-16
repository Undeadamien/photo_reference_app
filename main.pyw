import io
import json
import pathlib
import random
import sys

import requests

from module.reference_window import ReferenceWindow
from module.setup_window import SetupWindow

CONFIG_FILE: pathlib.Path = pathlib.Path(__file__).parent / "config.json"


def load_config(config_file: pathlib.Path):
    with config_file.open() as config:
        config = json.load(config)
    return config


def request(url: str, query: str, amount: int) -> list[io.BytesIO]:
    url = f"{url}?q={query}" if query else url
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
    config = load_config(CONFIG_FILE)
    image_path = pathlib.Path(config["path"])
    max_image = len(list(image_path.glob("*.jpg")))

    # launch the setup window and retrieve the parameters
    setup_w = SetupWindow(config["base_time"], config["base_amount"], max_image)
    time, amount = setup_w.run()

    # exit the app if not paramerters where selected
    if not (time and amount):
        sys.exit()

    # load the images from the selected source
    if config["online"]:
        images = request(config["api_url"], config["query"], amount)
    else:
        images = sample(image_path, amount)

    # launch the reference window
    ref_w = ReferenceWindow(time, images, config["position"], config["size"])
    ref_w.run()


if __name__ == "__main__":
    main()
