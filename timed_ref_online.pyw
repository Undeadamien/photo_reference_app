from module.reference_window import ReferenceWindow
from module.scryfall_api import request_image
from module.setup_window import SetupWindow


def main():
    mediator = []  # [time, amount]
    SetupWindow(mediator).run()
    ReferenceWindow(mediator[0], request_image(mediator[1])).run()


if __name__ == "__main__":
    main()
