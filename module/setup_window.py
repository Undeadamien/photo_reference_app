import tkinter as tk


class SetupWindow(tk.Tk):
    def __init__(
        self,
        max_image_choice: int,
        default_time: int,
        default_amount: int,
    ):
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
        self.time_and_amount = (0, 0)

        self.start_x, self.start_y = None, None

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
            to=min(max_image_choice, 10),
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

        # set draggable widget
        self.draggable_widgets: list[tk.Widget] = [
            self.time_label,
            self.amount_label,
        ]

        # set sliders values
        self.time_slider.set(default_time)
        self.amount_slider.set(default_amount)

        # place widgets on grid
        self.amount_label.grid(row=0, column=1, sticky="nesw")
        self.amount_slider.grid(row=1, column=1, sticky="nesw")
        self.confirm_button.grid(row=3, column=0, columnspan=2, sticky="nesw")
        self.time_label.grid(row=0, sticky="nesw")
        self.time_slider.grid(row=1, column=0, sticky="nesw")

        # bind action to function
        self.bind("<B1-Motion>", self.do_move)
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<ButtonRelease-1>", self.stop_move)
        self.bind("<Return>", lambda _: self.confirm())

    def confirm(self) -> None:
        self.time_and_amount = [self.time_slider.get(), self.amount_slider.get()]
        self.after(0, self.destroy)  # avoid an race condition with ButtonRelease bind

    def recenter(self) -> None:
        self.update()  # update to get the actual size of the window
        p_x = self.winfo_screenwidth() // 2 - self.winfo_width() // 2
        p_y = self.winfo_screenheight() // 2 - self.winfo_height() // 2
        self.geometry(f"+{p_x}+{p_y}")

    def run(self) -> tuple[int, int]:
        self.recenter()
        self.mainloop()

        return self.time_and_amount

    def start_move(self, event) -> None:
        def click_on(wid: tk.Widget):
            m_x = self.winfo_pointerx() - self.winfo_rootx()
            m_y = self.winfo_pointery() - self.winfo_rooty()
            if not (wid.winfo_x() < m_x < wid.winfo_x() + wid.winfo_width()):
                return False
            if not (wid.winfo_y() < m_y < wid.winfo_y() + wid.winfo_height()):
                return False
            return True

        if any(map(click_on, self.draggable_widgets)):
            self.start_x, self.start_y = event.x, event.y
        else:
            self.start_x, self.start_y = None, None

    def do_move(self, event) -> None:
        if self.start_y and self.start_x:
            p_x = self.winfo_x() + event.x - self.start_x
            p_y = self.winfo_y() + event.y - self.start_y
            self.geometry(f"+{p_x}+{p_y}")

    def stop_move(self, _) -> None:
        self.start_x, self.start_y = None, None
