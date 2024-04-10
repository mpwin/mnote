import argparse
import os
import tkinter as tk
import yaml

from .app import App


def parse_args() -> argparse.Namespace:
    """Parses command-line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    return parser.parse_args()


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


def main() -> None:
    args: argparse.Namespace = parse_args()

    with open(args.path, encoding='utf-8') as f:
        data: dict = yaml.safe_load(f)

    app: App = App(args.path, data)
    center_window(app)
    app.mainloop()


if __name__ == '__main__':
    main()
