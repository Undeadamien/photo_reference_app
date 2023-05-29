"""Module containing a personnalized Tk window"""

from tkinter import Button, Label, Tk, Scale


class SetupWindow(Tk):
    """When closed add the values of the two scales to the mediator"""

    def __init__(
        self,
        mediator: list,
        max_image: int,
        default_time: int = 15,
        default_amount: int = 4,
    ):
        super().__init__()

        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.overrideredirect(True)
        self.focus_force()

        self.mediator = mediator

        self.start_x, self.start_y = None, None

        self.configure(
            bg="black",
            highlightcolor="black",
            highlightbackground="black",
            highlightthickness=2,
        )

        self.time_slider = Scale(
            self,
            font=("Small Fonts", 10, "bold"),
            fg="black",
            bg="white",
            sliderrelief="solid",
            troughcolor="grey",
            highlightthickness=2,
            highlightbackground="black",
            showvalue=False,
            from_=5,
            to=60,
            orient="horizontal",
            length=300,
            tickinterval=5,
            bigincrement=5,
            resolution=5,
        )

        self.amount_slider = Scale(
            self,
            bg="white",
            fg="black",
            sliderrelief="solid",
            troughcolor="grey",
            highlightthickness=2,
            highlightbackground="black",
            font=("Small Fonts", 10, "bold"),
            showvalue=False,
            from_=1,
            to=min(max_image, 10),
            tickinterval=1,
            orient="horizontal",
            length=300,
        )

        self.time_label = Label(
            self,
            bg="white",
            fg="black",
            highlightthickness=2,
            highlightbackground="black",
            font=("Small Fonts", 15, "bold"),
            text="MINUTES",
        )

        self.amount_label = Label(
            self,
            text="IMAGES",
            font=("Small Fonts", 15, "bold"),
            fg="black",
            bg="white",
            highlightthickness=2,
            highlightbackground="black",
        )

        self.confirm_button = Button(
            self,
            text="CONFIRM",
            font=("Small Fonts", 15, "bold"),
            relief="solid",
            fg="black",
            bg="white",
            highlightthickness=1,
            command=self.confirm,
        )

        self.time_slider.set(default_time)
        self.amount_slider.set(default_amount)

        self.time_label.grid(row=0, sticky="nesw")
        self.amount_label.grid(row=0, column=1, sticky="nesw")
        self.time_slider.grid(row=1, column=0, sticky="nesw")
        self.amount_slider.grid(row=1, column=1, sticky="nesw")
        self.confirm_button.grid(row=2, column=0, columnspan=2, sticky="nesw")

        self.bind("<Return>", lambda _: self.confirm())
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.do_move)
        self.bind("<ButtonRelease-1>", self.stop_move)

    def confirm(self) -> None:
        """Confirm the paramters and close the current window"""

        self.mediator += [self.time_slider.get(), self.amount_slider.get()]
        self.after(0, self.destroy)  # avoid an error with ButtonRelease bind

    def recenter(self) -> None:
        """Replace the window in the middle of the screen"""

        self.update()  # update to get the real size of the window
        pos_x = self.winfo_screenwidth() // 2 - self.winfo_width() // 2
        pos_y = self.winfo_screenheight() // 2 - self.winfo_height() // 2
        self.geometry(f"+{pos_x}+{pos_y}")

    def run(self):
        """Wrapper for recenter and mainloop"""

        self.recenter()
        self.mainloop()

    def start_move(self, event) -> None:
        """Store the position of the mouse relative to the window"""

        # mouse position, relative to the top-left corner of the window
        mouse_x = self.winfo_pointerx() - self.winfo_rootx()
        mouse_y = self.winfo_pointery() - self.winfo_rooty()

        # filter where the dragging can start
        # in this case we exclude the sliders and the button
        valid_x = 0 < mouse_x < self.winfo_width()
        valid_y = 0 < mouse_y < self.time_label.winfo_height()

        if valid_x and valid_y:
            self.start_x, self.start_y = event.x, event.y
        else:
            self.start_x, self.start_y = None, None

    def do_move(self, event) -> None:
        """Move the window"""

        if self.start_y and self.start_x:
            pos_x = self.winfo_x() + event.x - self.start_x
            pos_y = self.winfo_y() + event.y - self.start_y
            self.geometry(f"+{pos_x}+{pos_y}")

    def stop_move(self, _) -> None:
        """Reset self.start_x and self.start_y"""

        self.start_x, self.start_y = None, None
