"""Module containing a personnalized Tk window"""

from random import sample
from tkinter import Button, Canvas, Label, Tk
from PIL import Image, ImageTk


class ReferenceWindow(Tk):
    """Display x images during y minutes"""

    def __init__(
        self,
        mediator: list,
        files: list[str],
        image_position: tuple = (0, 40),
        image_size: tuple = (350, 500),
    ):
        super().__init__()

        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.geometry(f"+{image_position[0]}+{image_position[1]}")
        self.focus_force()

        duration, amount, *_ = mediator

        self.duration: int = duration * 60 + 1
        self.remaining_time: int = self.duration
        self.timer_update_call = None
        self.paused: bool = False

        self.image_position = image_position  # top-left corner
        self.image_size = image_size

        self.images = self.convert_image(sample(files, amount))
        self.current_image = 0  # store which image is currently displayed

        self.start_x, self.start_y = None, None

        self.configure(
            bg="black",
            highlightcolor="black",
            highlightbackground="black",
            highlightthickness=2,
        )

        # place holder for the timer
        self.timer = Label(self)

        # widget used to cover the image when the timer is paused
        self.cover = Canvas(
            self,
            bg="black",
            border=0,
            highlightthickness=1,
            highlightbackground="white",
            highlightcolor="black",
        )

        self.picture = Label(
            self,
            image=self.images[self.current_image],
            highlightbackground="black",
            bg="black",
        )

        self.exit_button = Button(
            self,
            text="X",
            bg="white",
            fg="black",
            font=("Small Fonts", 10, "bold"),
            highlightcolor="black",
            highlightbackground="white",
            relief="flat",
            height=1,
            width=2,
            command=self.destroy,
        )

        self.pause_button = Button(
            self,
            text="II",
            bg="white",
            fg="black",
            font=("Small Fonts", 10, "bold"),
            highlightcolor="black",
            highlightbackground="white",
            relief="flat",
            height=1,
            width=2,
            command=self.pause,
        )

        self.grid_columnconfigure(1, weight=2)

        self.timer.grid(row=0, column=1, sticky="nesw")
        self.picture.grid(row=1, column=0, columnspan=3)
        self.pause_button.grid(row=0, column=0, sticky="nesw", pady=2, padx=2)
        self.exit_button.grid(row=0, column=2, sticky="nesw", pady=2, padx=2)

        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.do_move)
        self.bind("<ButtonRelease-1>", self.stop_move)

    def convert_image(self, images: list) -> list[ImageTk.PhotoImage]:
        """Convert and return, a list of image file into ImageTk.PhotoImage"""

        converted_images = []

        for image in images:
            image = Image.open(image)
            image.thumbnail(self.image_size)

            converted_images.append(ImageTk.PhotoImage(image))

        return converted_images

    def pause(self) -> None:
        """Pause the timer cover the image"""

        self.paused = not self.paused

        if self.paused:
            self.after_cancel(self.timer_update_call)
            self.picture.grid_forget()
            self.cover.grid(row=1, column=0, columnspan=3)

            height = self.picture.winfo_height() - 2
            width = self.picture.winfo_width() - 2
            self.cover.configure(height=height, width=width)

        else:
            self.cover.grid_forget()
            self.picture.grid(row=1, column=0, columnspan=3)
            self.timer_update_call = self.after(500, self.update_timer)

    def update_image(self) -> None:
        """Pass to the next image and reset the timer"""

        self.current_image += 1

        if self.current_image >= len(self.images):
            self.destroy()

        else:
            self.picture.configure(image=self.images[self.current_image])

    def update_timer(self) -> None:
        """Call it self recursively, updating the time and the timer label"""

        self.remaining_time -= 1
        minutes, seconds = divmod(self.remaining_time, 60)

        self.timer.configure(
            text=f"{(minutes):02}:{(seconds):02}",
            font=("Small Fonts", 15, "bold"),
            bg="white",
            highlightbackground="black",
            highlightthickness=2,
        )

        if self.remaining_time >= 0:
            self.timer_update_call = self.after(1000, self.update_timer)

        else:
            self.after_cancel(self.timer_update_call)
            self.remaining_time = self.duration
            self.update_timer()
            self.update_image()

    def run(self) -> None:
        """Wrapper for update_timer and mainloop"""

        self.update_timer()
        self.mainloop()

    def start_move(self, event) -> None:
        """Store the position of the mouse relative to the window"""

        self.start_x, self.start_y = event.x, event.y

    def do_move(self, event) -> None:
        """Move the window"""

        pos_x = self.winfo_x() + event.x - self.start_x
        pos_y = self.winfo_y() + event.y - self.start_y
        self.geometry(f"+{pos_x}+{pos_y}")

    def stop_move(self, _) -> None:
        """Reset self.start_x and self.start_y"""

        self.start_x, self.start_y = None, None
