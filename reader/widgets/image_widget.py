import tkinter as tk
from pathlib import Path
from PIL import Image
from PIL.ImageTk import PhotoImage

from .base_widget import BaseWidget


class ImageWidget(BaseWidget):
    """Widget for displaying images.

    Attributes:
        image: The Image object opened from the file specified in data.
        photo_image: The PhotoImage object used for displaying the image in
            Tkinter.
    """

    def __init__(self, parent, data: dict, mnote_directory: Path) -> None:
        """Initializes a new ImageWidget instance.

        Args:
            parent: Parent widget.
            data: Configuration and content for the widget.
            mnote_directory: The directory path of the mnote.
        """
        super().__init__(parent, data)

        self.image: Image = Image.open(mnote_directory / data['path'])
        self.photo_image: PhotoImage = PhotoImage(self.image)
        self.display_image(self.photo_image, self.data.get('hide'))

        self.config(self.frame_config)
        self.pack_propagate(False)
        self.pack(self.pack_config)

    @property
    def frame_config(self) -> dict:
        return {
            'height': self.data.get('height', self.image.height),
            'width': self.data.get('width', self.image.width),
            }

    @property
    def label_config(self) -> dict:
        return {
            'bg': self.background,
            'fg': self.foreground,
            'font': ('Consolas', 16),
            'text': "",
            }

    def display_image(self, image: PhotoImage, hide: str | None) -> None:
        label: tk.Label = tk.Label(self, **self.label_config)

        if hide:
            label.config(text=hide, bg='black')
            label.bind('<Button-1>', lambda e: self.reveal_image(label, image))
        else:
            label.config(image=image)

        label.pack(expand=True, fill='both')

    def reveal_image(self, label: tk.Label, image: PhotoImage) -> None:
        label.config(image=image, **self.label_config)
