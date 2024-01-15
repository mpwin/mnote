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
        self.config(bg='#1e1e1e')

        if 'header' in data:
            self.header = self.make_header(data['header'])
        for panel in data.get('panels', []):
            match panel['type']:
                case 'image':
                    self.panels.append(self.make_image_panel(panel['data']))
                case 'recall':
                    self.panels.append(self.make_recall_panel(panel['data']))
                case 'text':
                    self.panels.append(self.make_text_panel(panel['data']))

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

    def make_image_panel(self, data: dict) -> tk.Frame:
        """Creates and displays an image panel from the input data.

        Args:
            data: The data and config of the image panel to be displayed.

        Returns:
            The image panel's root tkinter.Frame object.
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
            bg='#000000',
            fg='#d4d4d4',
            font=('Consolas', 16),
            )
        label.image = photo_image # Keep a reference to the image

        if 'hide' in data:
            label.config(text=data['hide'])
            label.bind('<Button-1>', lambda event: label.config(
                image=photo_image, text="",
                ))
        else:
            label.config(image=photo_image)

        label.pack(expand=True, fill='both')
        frame.pack_propagate(False)
        frame.pack(side='left')
        return frame

    def make_recall_panel(self, data: dict) -> tk.Frame:
        """Creates and displays a recall panel from the input data.

        Args:
            data: The data and config of the recall panel to be displayed.

        Returns:
            The recall panel's root tkinter.Frame object.
        """
        recall_frame: tk.Frame = tk.Frame(
            self,
            bg='#1e1e1e',
            height=80*len(data['items'])+40,
            padx=40,
            pady=20,
            width=400,
            )

        for item in data['items']:
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

    def make_text_panel(self, data: dict) -> tk.Frame:
        """Creates and displays a text panel from the input data.

        Args:
            data: The data and config of the text panel to be displayed.

        Returns:
            The text panel's root tkinter.Frame object.
        """
        frame: tk.Frame = tk.Frame(self)
        body: tk.Label = tk.Label(
            frame,
            bg='#1e1e1e',
            fg='#d4d4d4',
            font=('Consolas', 16),
            justify='left',
            padx=40,
            pady=20,
            text=data['text'],
            wraplength=800,
            )
        body.pack()
        frame.pack(side='left')
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
