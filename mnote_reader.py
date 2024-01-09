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
        self.panels: list = []
        self.title("mnote")

        if 'header' in data:
            self.header = self.make_header(data['header'])
        for panel in data.get('panels', []):
            match panel['type']:
                case 'image':
                    self.panels.append(self.make_image(panel['data']))
                case 'text':
                    self.panels.append(self.make_body(panel['text']))
                case 'recall':
                    self.panels.append(self.make_recall(panel['items']))

        if 'image' in data:
            self.image = self.make_image(data['image'])
        if 'body' in data:
            self.body = self.make_body(data['body'])
        if 'recall' in data:
            self.recall = self.make_recall(data['recall'])

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

    def make_image(self, data: dict) -> tuple[tk.Frame, ImageTk.PhotoImage]:
        """Creates and displays an image panel from the input data.

        Args:
            data: The data and config of the image panel to be displayed.

        Returns:
            A tuple that contains the panel's root tkinter.Frame object and a
            reference to the image's ImageTk.PhotoImage object.
        """
        image: Image = Image.open(f"{self.path}/{data['name']}")
        photo_image: ImageTk.PhotoImage = ImageTk.PhotoImage(image)
        frame: tk.Frame = tk.Frame(
            self,
            height=image.height,
            width=image.width,
            )
        label: tk.Label = tk.Label(
            frame,
            image=photo_image,
            )
        label.pack()
        frame.pack_propagate(False)
        frame.pack(side='left')
        return (frame, photo_image)

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
        body.pack(expand=True, fill='both', side='left')
        return body

    def make_recall(self, items: list[dict]) -> tk.Frame:
        """Creates and displays a recall frame with the specified Q&A items.

        Args:
            items: The list of Q&A items.

        Returns:
            The recall tkinter.Frame object.
        """
        recall_frame: tk.Frame = tk.Frame(
            self,
            bg='#1e1e1e',
            padx=40,
            pady=20,
            width=400,
            )

        for item in items:
            item_frame: tk.Frame = tk.Frame(
                recall_frame,
                bg='#1e1e1e',
                height=80,
                )
            item_frame.pack_propagate(False)
            item_frame.pack(fill='x')

            q: str = item['q']
            a: str = item['a']

            q_label: tk.Label = tk.Label(
                item_frame,
                anchor='w',
                bg='#1e1e1e',
                fg='#569cd6',
                font=('Consolas', 16),
                text=q,
                )
            q_label.pack(fill='x')

            a_label: tk.Label = tk.Label(
                item_frame,
                anchor='w',
                bg='#1e1e1e',
                fg='#d4d4d4',
                font=('Consolas', 16),
                text=a,
                )

            button: tk.Button = tk.Button(
                item_frame,
                activebackground='#569cd6',
                activeforeground='#d4d4d4',
                bg='#1e1e1e',
                fg='#d4d4d4',
                font=('Consolas', 12),
                text="Recall",
                )
            button.config(
                command=lambda label=a_label, text=a, button=button: (
                    label.pack(fill='x'),
                    button.pack_forget(),
                    )
                )
            button.pack(fill='x')

        recall_frame.pack_propagate(False)
        recall_frame.pack(fill='y', side='left')
        return recall_frame


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
