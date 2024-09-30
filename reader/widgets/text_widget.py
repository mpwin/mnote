import tkinter as tk

from .base_widget import BaseWidget


class TextWidget(BaseWidget):
    """Widget for displaying text."""

    def __init__(self, parent, data: dict) -> None:
        """Initializes a new TextWidget instance.

        Args:
            parent: Parent widget.
            data: Configuration and content for the widget.
        """
        super().__init__(parent, data)

        text: tk.Text = tk.Text(self)
        text.insert(tk.END, self.data['text'])
        text.config(self.text_config)
        text.pack()

        self.config(self.frame_config)
        self.pack(self.pack_config)

    @property
    def text_config(self) -> dict:
        return {
            'bd': 0,
            'bg': self.background,
            'fg': self.font_color,
            'font': (self.font, self.font_size),
            'height': self.text_height,
            'state': 'disabled',
            'width': self.text_width,
            'wrap': 'word',
            }

    @property
    def text_height(self) -> int:
        return len(self.data['text'].split('\n'))

    @property
    def text_width(self) -> int:
        return max([len(line) for line in self.data['text'].split('\n')])
