import argparse
import tkinter as tk
import yaml
from PIL import Image, ImageTk


def parse_args() -> argparse.Namespace:
    """
    Parses command-line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    return parser.parse_args()


def main():
    args: argparse.Namespace = parse_args()

    with open(args.path) as f:
        data: dict = yaml.safe_load(f)

    root = tk.Tk()
    root.title("mnote")

    if 'image' in data:
        image: Image = Image.open(data['image'])
        image_tk: ImageTk.PhotoImage = ImageTk.PhotoImage(image)
        image_label: tk.Label = tk.Label(root, image=image_tk)
        image_label.pack(side='left')

    note: tk.Label = tk.Label(
        root,
        font=('Lucida Console', 16),
        justify='left',
        text=data['body'],
        padx=40,
        pady=20,
        wraplength=800,
        )
    note.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
