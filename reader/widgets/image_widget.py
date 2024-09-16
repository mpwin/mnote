import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

from .base_widget import BaseWidget


class ImageWidget(BaseWidget):
    """Widget for displaying images.

    Attributes:
        image: The Image object opened from the file specified in data.
        photo_image: The PhotoImage object used for displaying the image in
            Tkinter.
        label: A Tkinter Label widget used for either displaying the image or a
            placeholder text.
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
        self.photo_image: ImageTk.PhotoImage = ImageTk.PhotoImage(self.image)
        self.label: tk.Label = self.create_label(self.photo_image)

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
            'bg': '#000000',
            'fg': '#d4d4d4',
            'font': ('Consolas', 16),
            }

    def create_label(self, image: ImageTk.PhotoImage) -> tk.Label:
        label: tk.Label = tk.Label(self, **self.label_config)

        if 'hide' in self.data:
            label.config(text=self.data['hide'])
            label.bind(
                '<Button-1>',
                lambda e: label.config(image=image, text="", bg='#1e1e1e'),
                )
        else:
            label.config(image=image)

        label.pack(expand=True, fill='both')
        return label
