from os import listdir
from os.path import join

from reference_window import ReferenceWindow
from setup_window import SetupWindow


IMAGE_PATH: str = r"C:\Users\Damien\Drawing\Photo_ref"
IMAGE_EXTENSION: tuple[str] = (".jpg", ".png")
IMAGES: list[str] = [
    join(IMAGE_PATH, image_name)
    for image_name in listdir(IMAGE_PATH)
    if image_name.lower().endswith(IMAGE_EXTENSION)
]
assert IMAGES


def test_mediator(mediator):
    assert mediator[1] <= len(IMAGES)
    assert isinstance(mediator, (list, tuple))
    assert len(mediator) == 2
    assert all(isinstance(x, int) for x in mediator)


def main():
    mediator = []  # [time, amount]

    SetupWindow(mediator, max_image=len(IMAGES)).run()
    test_mediator(mediator)
    ReferenceWindow(mediator, IMAGES).run()


if __name__ == "__main__":
    main()
