import tkinter as tk


class DraggableWidgetHandler:
    def __init__(self, parent: tk.Tk, start_widgets: list[tk.Widget]):
        self.parent = parent
        self.drag_start_widgets = start_widgets

        # used to keep the mouse in place relative to the window
        self.start_x, self.start_y = None, None

    def start_move(self, event):
        def mouse_on(wid: tk.Widget):
            m_x = self.parent.winfo_pointerx() - self.parent.winfo_rootx()
            m_y = self.parent.winfo_pointery() - self.parent.winfo_rooty()
            if not (wid.winfo_x() < m_x < wid.winfo_x() + wid.winfo_width()):
                return False
            if not (wid.winfo_y() < m_y < wid.winfo_y() + wid.winfo_height()):
                return False
            return True

        # set a starting point if mouse on any valid widget
        if any(map(mouse_on, self.drag_start_widgets)):
            self.start_x, self.start_y = event.x, event.y
        else:
            self.start_x, self.start_y = None, None

    def do_move(self, event):
        if not (self.start_y and self.start_x):
            return
        p_x = self.parent.winfo_x() + event.x - self.start_x
        p_y = self.parent.winfo_y() + event.y - self.start_y
        self.parent.geometry(f"+{p_x}+{p_y}")

    def stop_move(self, _):
        self.start_x, self.start_y = None, None
