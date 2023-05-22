from tkinter import Button, Label, Tk, Scale


class SetupWindow(Tk):

    def __init__(self,
                 mediator: list,
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
            highlightthickness=2
        )

        self.time_slider = Scale(self,
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
                                 resolution=5
                                 )

        self.amount_slider = Scale(self,
                                   bg="white",
                                   fg="black",
                                   sliderrelief="solid",
                                   troughcolor="grey",
                                   highlightthickness=2,
                                   highlightbackground="black",
                                   font=("Small Fonts", 10, "bold"),
                                   showvalue=False,
                                   from_=1,
                                   to=10,
                                   tickinterval=1,
                                   orient="horizontal",
                                   length=300
                                   )

        self.time_label = Label(self,
                                bg="white",
                                fg="black",
                                highlightthickness=2,
                                highlightbackground="black",
                                font=("Small Fonts", 15, "bold"),
                                text="MINUTES"
                                )

        self.amount_label = Label(self,
                                  text="IMAGES",
                                  font=("Small Fonts", 15, "bold"),
                                  fg="black",
                                  bg="white",
                                  highlightthickness=2,
                                  highlightbackground="black"
                                  )

        self.confirm_button = Button(self,
                                     text="CONFIRM",
                                     font=("Small Fonts", 15, "bold"),
                                     relief="solid",
                                     fg="black",
                                     bg="white",
                                     highlightthickness=1,
                                     command=self.confirm
                                     )

        # set the starting value of the sliders
        self.time_slider.set(default_time)
        self.amount_slider.set(default_amount)

        # place every widget and recenter the window
        self.time_label.grid(row=0, sticky="nesw")
        self.amount_label.grid(row=0, column=1, sticky="nesw")
        self.time_slider.grid(row=1, column=0, sticky="nesw")
        self.amount_slider.grid(row=1, column=1, sticky="nesw")
        self.confirm_button.grid(row=2, column=0, columnspan=2, sticky="nesw")
        self.recenter()

        self.bind("<Return>", lambda _: self.confirm())
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.do_move)
        self.bind("<ButtonRelease-1>", self.stop_move)

    def confirm(self) -> None:
        self.mediator.append(self.time_slider.get())
        self.mediator.append(self.amount_slider.get())
        self.after(0, self.destroy)

    def recenter(self) -> None:
        self.update()  # update to get the real size of the window
        pos_x = self.winfo_screenwidth()//2-self.winfo_width()//2
        pos_y = self.winfo_screenheight()//2-self.winfo_height()//2
        self.geometry(f"+{pos_x}+{pos_y}")

    def run(self):
        self.mainloop()

    def start_move(self, event) -> None:
        # mouse position, relative to the top-left corner of the window
        mouse_x = self.winfo_pointerx() - self.winfo_rootx()
        mouse_y = self.winfo_pointery() - self.winfo_rooty()
        # filter where the dragging can start
        # in this case we exclude the sliders and the button
        left_x, right_x = 0, self.winfo_width()
        left_y, right_y = 0, self.time_label.winfo_height()

        if left_x < mouse_x < right_x and left_y < mouse_y < right_y:
            self.start_x, self.start_y = event.x, event.y
        else:
            self.start_x, self.start_y = None, None

    def do_move(self, event) -> None:
        if self.start_y and self.start_x:
            self.geometry(f"+{self.winfo_x() + event.x - self.start_x}" +
                          f"+{self.winfo_y() + event.y - self.start_y}")

    def stop_move(self, _) -> None:
        self.start_x, self.start_y = None, None
