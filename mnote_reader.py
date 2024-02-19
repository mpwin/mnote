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
        self.path: str = path
        self.panels: list = []
        self.title("mnote")
        self.config(bg='#1e1e1e')
        self.protocol('WM_DELETE_WINDOW', self.on_close)

        if 'header' in data:
            self.header = self.make_header(data['header'])
        for panel in data.get('panels', []):
            match panel['type']:
                case 'image':
                    self.panels.append(ImagePanel(self, panel['data']))
                case 'recall':
                    self.panels.append(RecallPanel(self, panel['data']))
                case 'text':
                    self.panels.append(TextPanel(self, panel['data']))

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

    def on_close(self) -> None:
        """Handles the event triggered by closing the Tkinter window."""
        print(self.path)
        self.destroy()


class Panel(tk.Frame):
    """The base class for the different types of Mnote panels.

    Attributes:
        app: A reference to the main Mnote App instance.
        data: A dict containing configuration and content for the panel.
    """

    def __init__(self, app: App, data: dict) -> None:
        """Initializes a new Panel instance.

        Args:
            app: The main Mnote App instance.
            data: Configuration and content for the panel.
        """
        super().__init__(app)
        self.app: App = app
        self.data: dict = data


class ImagePanel(Panel):
    """A subclass of Panel specialized for displaying images.

    Attributes:
        image: The Image object opened from the file specified in data.
        photo_image: The PhotoImage object used for displaying the image in
            Tkinter.
        label: A Tkinter Label widget used for either displaying the image or a
            placeholder text.
    """

    def __init__(self, app: App, data: dict) -> None:
        """Initializes a new ImagePanel instance.

        Args:
            app: The main Mnote App instance.
            data: Configuration and content for the panel.
        """
        super().__init__(app, data)

        self.image: Image = Image.open(f"{self.app.path}/{data['name']}")
        self.photo_image: ImageTk.PhotoImage = ImageTk.PhotoImage(self.image)
        self.config(
            height=data.get('height', self.image.height),
            width=data.get('width', self.image.width),
            )
        self.label: tk.Label = tk.Label(
            self,
            bg='#000000',
            fg='#d4d4d4',
            font=('Consolas', 16),
            )

        if 'hide' in data:
            self.label.config(text=data['hide'])
            self.label.bind('<Button-1>', lambda event: self.label.config(
                image=self.photo_image, text="",
                ))
        else:
            self.label.config(image=self.photo_image)

        self.label.pack(expand=True, fill='both')
        self.pack_propagate(False)
        self.pack(side='left')


class RecallPanel(Panel):
    """A subclass of Panel specialized for displaying recall items."""

    def __init__(self, app: App, data: dict) -> None:
        """Initializes a new RecallPanel instance.

        Args:
            app: The main Mnote App instance.
            data: Configuration and content for the panel.
        """
        super().__init__(app, data)

        self.config(
            bg='#1e1e1e',
            height=80*len(data['items'])+40,
            padx=40,
            pady=20,
            width=400,
            )

        for item in data['items']:
            item_frame: tk.Frame = tk.Frame(
                self,
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

        self.pack_propagate(False)
        self.pack(fill='y', side='left')


class TextPanel(Panel):
    """A subclass of Panel specialized for displaying text."""

    def __init__(self, app: App, data: dict) -> None:
        """Initializes a new TextPanel instance.

        Args:
            app: The main Mnote App instance.
            data: Configuration and content for the panel.
        """
        super().__init__(app, data)

        body: tk.Label = tk.Label(
            self,
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
        self.pack(side='left')


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
    name: str = os.path.basename(args.path).split('.')[0]

    with open(f"{args.path}/{name}.yaml", encoding='utf-8') as f:
        data: dict = yaml.safe_load(f)

    app: App = App(args.path, data)
    center_window(app)
    app.mainloop()


if __name__ == '__main__':
    main()
