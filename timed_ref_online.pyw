from module.reference_window import ReferenceWindow
from module.scryfall_api import request_image
from module.setup_window import SetupWindow


def run_application():
    time_and_amount = []
    SetupWindow(time_and_amount).run()
    ReferenceWindow(time_and_amount[0], request_image(time_and_amount[1])).run()


if __name__ == "__main__":
    run_application()
