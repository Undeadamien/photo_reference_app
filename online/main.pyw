from api_module import request_image
from reference_window import ReferenceWindow
from setup_window import SetupWindow


def main():
    mediator = []  # [time, amount]

    SetupWindow(mediator).run()
    ReferenceWindow(mediator[0], request_image(mediator[1])).run()


if __name__ == "__main__":
    main()
