import argparse
import os
import tkinter as tk
import yaml
from PIL import Image, ImageTk


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


def main():
    args: argparse.Namespace = parse_args()
    name: str = os.path.basename(args.path).split('.')[0]

    with open(f"{args.path}/{name}.yaml") as f:
        data: dict = yaml.safe_load(f)

    root = tk.Tk()
    root.title("mnote")

    if 'title' in data:
        title: tk.Label = tk.Label(
            root,
            bg='#2d2d2d',
            fg='#ffffff',
            font=('Consolas', 16),
            text=data['title'],
            )
        title.pack(fill='both')

    if 'image' in data:
        image: Image = Image.open(f"{args.path}/{data['image']}")
        image_tk: ImageTk.PhotoImage = ImageTk.PhotoImage(image)
        image_label: tk.Label = tk.Label(root, image=image_tk, borderwidth=0)
        image_label.pack(side='left')

    if 'body' in data:
        note: tk.Label = tk.Label(
            root,
            bg='#1e1e1e',
            fg='#d4d4d4',
            font=('Consolas', 16),
            justify='left',
            padx=40,
            pady=20,
            text=data['body'],
            wraplength=800,
            )
        note.pack(expand=True, fill='both')

    center_window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
