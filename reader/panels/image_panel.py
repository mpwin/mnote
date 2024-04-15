import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

from .base_panel import BasePanel


class ImagePanel(BasePanel):
    """A subclass of BasePanel specialized for displaying images.

    Attributes:
        image: The Image object opened from the file specified in data.
        photo_image: The PhotoImage object used for displaying the image in
            Tkinter.
        label: A Tkinter Label widget used for either displaying the image or a
            placeholder text.
    """

    def __init__(self, app: 'App', data: dict, mnote_directory: Path) -> None:
        """Initializes a new ImagePanel instance.

        Args:
            app: The main Mnote App instance.
            data: Configuration and content for the panel.
            mnote_directory: The directory path of the mnote.
        """
        super().__init__(app, data)

        self.image: Image = Image.open(mnote_directory / data['path'])
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
                image=self.photo_image, text="", bg='#1e1e1e',
                ))
        else:
            self.label.config(image=self.photo_image)

        self.label.pack(expand=True, fill='both')
        self.pack_propagate(False)
        self.pack(side='left')
