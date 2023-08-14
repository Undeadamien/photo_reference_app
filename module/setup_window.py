import tkinter as tk

from module.drag_handler import DraggableWidgetHandler


class SetupWindow(tk.Tk):
    def __init__(self, default_time: int, default_amount: int, max_image: int):
        super().__init__()

        # configure window
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.overrideredirect(True)
        self.focus_force()
        self.configure(
            bg="black",
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=2,
        )

        # attributes
        self.return_values = [0, 0]

        # widgets
        self.time_slider = tk.Scale(
            self,
            bg="white",
            bigincrement=5,
            fg="black",
            font=("Small Fonts", 10, "bold"),
            from_=5,
            highlightbackground="black",
            highlightthickness=2,
            length=300,
            orient="horizontal",
            resolution=5,
            showvalue=False,
            sliderrelief="solid",
            tickinterval=5,
            to=60,
            troughcolor="grey",
        )

        self.amount_slider = tk.Scale(
            self,
            bg="white",
            fg="black",
            font=("Small Fonts", 10, "bold"),
            from_=1,
            highlightbackground="black",
            highlightthickness=2,
            length=300,
            orient="horizontal",
            showvalue=False,
            sliderrelief="solid",
            tickinterval=1,
            to=min(max_image, 10),
            troughcolor="grey",
        )

        self.time_label = tk.Label(
            self,
            bg="white",
            fg="black",
            font=("Small Fonts", 15, "bold"),
            highlightbackground="black",
            highlightthickness=2,
            text="MINUTES",
        )

        self.amount_label = tk.Label(
            self,
            bg="white",
            fg="black",
            font=("Small Fonts", 15, "bold"),
            highlightbackground="black",
            highlightthickness=2,
            text="IMAGES",
        )

        self.confirm_button = tk.Button(
            self,
            bg="white",
            command=self.confirm,
            fg="black",
            font=("Small Fonts", 15, "bold"),
            highlightthickness=1,
            relief="solid",
            text="CONFIRM",
        )

        # setup the drag handler
        draggable_widgets = [self.time_label, self.amount_label]
        self.drag_handler = DraggableWidgetHandler(self, draggable_widgets)

        # set sliders values
        self.time_slider.set(default_time)
        self.amount_slider.set(default_amount)

        # place widgets on grid
        self.time_label.grid(row=0, sticky="nesw")
        self.amount_label.grid(row=0, column=1, sticky="nesw")
        self.time_slider.grid(row=1, column=0, sticky="nesw")
        self.amount_slider.grid(row=1, column=1, sticky="nesw")
        self.confirm_button.grid(row=3, column=0, columnspan=2, sticky="nesw")

        # bind action to function
        self.bind("<ButtonPress-1>", self.drag_handler.start_move)
        self.bind("<B1-Motion>", self.drag_handler.do_move)
        self.bind("<ButtonRelease-1>", self.drag_handler.stop_move)
        self.bind("<Return>", lambda _: self.confirm())

    def confirm(self) -> None:
        self.return_values = [self.time_slider.get(), self.amount_slider.get()]
        self.after(0, self.destroy)

    def recenter(self) -> None:
        self.update()  # update to get the actual size of the window
        p_x = self.winfo_screenwidth() // 2 - self.winfo_width() // 2
        p_y = self.winfo_screenheight() // 2 - self.winfo_height() // 2
        self.geometry(f"+{p_x}+{p_y}")

    def run(self) -> tuple[int, int]:
        self.recenter()
        self.mainloop()
        return self.return_values
