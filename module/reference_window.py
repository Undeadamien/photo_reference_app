import io
import tkinter as tk

from PIL import Image, ImageTk

from module.drag_handler import DraggableWidgetHandler


class ReferenceWindow(tk.Tk):
    def __init__(
        self,
        duration: int,
        image: list[io.BytesIO],
        position: tuple[int, int],
        size: tuple[int, int],
    ):
        super().__init__()

        # configure window
        self.attributes("-topmost", True)
        self.focus_force()
        self.overrideredirect(True)
        self.geometry(f"+{position[0]}+{position[1]}")
        self.configure(
            bg="black",
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=2,
        )

        # time
        self.duration: int = duration * 60 + 1
        self.paused: bool = False
        self.remaining_time: int = self.duration
        # image
        self.current_image: int = 0  # store which image is currently displayed
        self.position: tuple = position  # top-left corner
        self.size: tuple = size
        self.images: int = self.convert(image)
        # misc
        self.timer_update_call = None

        # widgets
        self.timer = tk.Label(self)  # place holder for the timer

        self.picture = tk.Label(
            self,
            bg="black",
            highlightbackground="black",
            image=self.images[self.current_image],
        )

        self.cover = tk.Canvas(
            self,
            bg="black",
            border=0,
            highlightbackground="white",
            highlightcolor="black",
            highlightthickness=1,
        )

        self.exit_button = tk.Button(
            self,
            bg="white",
            command=self.destroy,
            fg="black",
            font=("Small Fonts", 10, "bold"),
            height=1,
            highlightbackground="white",
            highlightcolor="black",
            relief="flat",
            text="X",
            width=2,
        )

        self.pause_button = tk.Button(
            self,
            bg="white",
            command=self.pause,
            fg="black",
            font=("Small Fonts", 10, "bold"),
            height=1,
            highlightbackground="white",
            highlightcolor="black",
            relief="flat",
            text="II",
            width=2,
        )

        # setup the drag handler
        draggable_widgets = [self.picture, self.timer, self.cover]
        self.drag_handler = DraggableWidgetHandler(self, draggable_widgets)

        # place widgets on grid
        self.grid_columnconfigure(1, weight=2)
        self.exit_button.grid(row=0, column=2, sticky="nesw", pady=2, padx=2)
        self.pause_button.grid(row=0, column=0, sticky="nesw", pady=2, padx=2)
        self.picture.grid(row=1, column=0, columnspan=3)
        self.timer.grid(row=0, column=1, sticky="nesw")

        self.bind("<ButtonPress-1>", self.drag_handler.start_move)
        self.bind("<B1-Motion>", self.drag_handler.do_move)
        self.bind("<ButtonRelease-1>", self.drag_handler.stop_move)
        # lambda _ to catch the event variabe send by bind
        self.bind("<Escape>", lambda _: self.destroy())
        self.bind("<space>", lambda _: self.pause())

    def convert(self, image: list[io.BytesIO]) -> list[ImageTk.PhotoImage]:
        converted_images = []

        for data in image:
            # load and strech the image
            image = Image.open(data)
            ratio = min(self.size[0] / image.width, self.size[1] / image.height)
            new_size = (int(image.width * ratio), int(image.height * ratio))
            image = ImageTk.PhotoImage(image.resize(new_size))
            converted_images.append(image)

        return converted_images

    def pause(self) -> None:
        self.paused = not self.paused

        if self.paused:
            self.after_cancel(self.timer_update_call)
            self.picture.grid_forget()
            self.cover.grid(row=1, column=0, columnspan=3)
            self.cover.configure(
                height=self.picture.winfo_height() - 2,
                width=self.picture.winfo_width() - 2,
            )

        else:
            self.cover.grid_forget()
            self.picture.grid(row=1, column=0, columnspan=3)
            self.timer_update_call = self.after(500, self.update_timer)

    def update_image(self) -> None:
        self.current_image += 1
        if self.current_image >= len(self.images):
            self.destroy()
        else:
            self.picture.configure(image=self.images[self.current_image])

    def update_timer(self) -> None:
        self.remaining_time -= 1
        minutes, seconds = divmod(self.remaining_time, 60)
        self.timer.configure(
            bg="white",
            font=("Small Fonts", 15, "bold"),
            highlightbackground="black",
            highlightthickness=2,
            text=f"{(minutes):02}:{(seconds):02}",
        )

        if self.remaining_time >= 0:
            self.timer_update_call = self.after(1000, self.update_timer)
        else:
            self.after_cancel(self.timer_update_call)
            self.remaining_time = self.duration
            self.update_timer()
            self.update_image()

    def run(self) -> None:
        self.update_timer()
        self.mainloop()
