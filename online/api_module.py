import io
from random import choice

import requests

image_data = []
api_key = "aqlpbk8h/oM6y1E4wYetNg==7XwdlZfKdnRYAZO3"
headers = {"X-Api-Key": api_key, "Accept": "image/jpg"}
api_url = "https://api.api-ninjas.com/v1/randomimage?"
categories = [
    "nature",
    "city",
    "technology",
    "food",
    "still_life",
    "wildlife",
]


def request_image(amount):
    for _ in range(amount):
        cat = choice(categories)
        response = requests.get(f"{api_url}category={cat}", headers=headers, timeout=30)
        image_data.append(io.BytesIO(response.content))

    return image_data
