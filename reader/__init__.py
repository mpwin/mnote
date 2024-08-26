import tkinter as tk
import yaml

from .app import App


def read(path: str) -> None:
    with open(path, encoding='utf-8') as f:
        data: dict = yaml.safe_load(f)

    app: App = App(path, data)
    center_window(app)
    app.mainloop()


def center_window(app: tk.Tk) -> None:
    """Center the tkinter application window on the screen.

    Args:
        app: The root tkinter.Tk object.
    """
    app.update_idletasks()
    window_w: int = app.winfo_width()
    window_h: int = app.winfo_height()
    screen_w: int = app.winfo_screenwidth()
    screen_h: int = app.winfo_screenheight()
    x: int = (screen_w//2) - (window_w//2)
    y: int = (screen_h//2) - (window_h//2)
    app.geometry("%dx%d+%d+%d" % (window_w, window_h, x, y))
