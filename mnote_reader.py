import argparse
import os
import tkinter as tk
import yaml
from PIL import Image, ImageTk


class App(tk.Tk):
    """A Tkinter application for displaying Mnote content."""

    def __init__(self, path: str, data: dict) -> None:
        """Initializes the App object based on its data argument.

        Args:
            path: The file system location of the Mnote.
            data: The deserialized data from the Mnote's YAML file.
        """
        super().__init__()
        self.path = path
        self.title("mnote")

        if 'header' in data:
            self.header = self.make_header(data['header'])
        if 'image' in data:
            self.image = self.make_image(data['image'])
        if 'body' in data:
            self.body = self.make_body(data['body'])

    def make_header(self, text: str) -> tk.Label:
        """Creates and displays a header label with the specified text.

        Args:
            text: The text to be displayed in the header label.

        Returns:
            The header tkinter.Label object.
        """
        header: tk.Label = tk.Label(
            self,
            bg='#2d2d2d',
            fg='#ffffff',
            font=('Consolas', 16),
            padx=8,
            pady=4,
            text=text,
            )
        header.pack(fill='both')
        return header

    def make_image(self, name: str) -> tuple[ImageTk.PhotoImage, tk.Label]:
        """Creates and displays a label that contains the specified image.

        Args:
            name: The name of the image to be drawn.

        Returns:
            A tuple that contains the image object and the tkinter.Label object
            that is holding the image.
        """
        image: Image = Image.open(f"{self.path}/{name}")
        photo_image: ImageTk.PhotoImage = ImageTk.PhotoImage(image)
        label: tk.Label = tk.Label(
            self,
            bg='#1e1e1e',
            borderwidth=0,
            image=photo_image,
            )
        label.pack(side='left', fill='both', expand=True)
        return (photo_image, label)

    def make_body(self, text: str) -> tk.Label:
        """Creates and displays a body label with the specified text.

        Args:
            text: The text to be displayed in the body label.

        Returns:
            The body tkinter.Label object.
        """
        body: tk.Label = tk.Label(
            self,
            bg='#1e1e1e',
            fg='#d4d4d4',
            font=('Consolas', 16),
            justify='left',
            padx=40,
            pady=20,
            text=text,
            wraplength=800,
            )
        body.pack(expand=True, fill='both')
        return body


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

    app: App = App(args.path, data)
    center_window(app)
    app.mainloop()


if __name__ == '__main__':
    main()
