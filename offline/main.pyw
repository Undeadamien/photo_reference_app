"""Application displaying random images, with a timer"""

from os import listdir
from os.path import join

from reference_window import ReferenceWindow
from setup_window import SetupWindow

PATH = r"C:\Users\Damien\Drawing\Photo_ref"
IMAGES = [join(PATH, file) for file in listdir(PATH) if file.endswith(".jpg")]
assert IMAGES, "No files or folders found to process"


def main():
    """Run the different window"""

    mediator = []  # [time, amount]
    SetupWindow(mediator, len(IMAGES)).run()
    ReferenceWindow(mediator, IMAGES).run()


if __name__ == "__main__":
    main()
