import random
import tkinter as tk

from .base_widget import BaseWidget


class SampleWidget(BaseWidget):
    """Widget for listing a random sample from a larger list of items."""

    def __init__(self, parent, data: dict) -> None:
        """Initializes a new SampleWidget instance.

        Args:
            parent: Parent widget.
            data: Configuration and content for the widget.
        """
        super().__init__(parent, data)

        sample: list = random.sample(self.data['items'], self.sample_size)
        self.display_items(sample)

        self.config(self.frame_config)
        self.pack(self.pack_config)

    @property
    def label_config(self) -> dict:
        return {
            'bg': self.background,
            'fg': self.font_color,
            'font': (self.font, self.font_size),
            'pady': 4,
            }

    @property
    def sample_size(self) -> int:
        return min(self.data.get('sample_size', 10), len(self.data['items']))

    def display_items(self, items: list) -> None:
        for item in items:
            label: tk.Label = tk.Label(self, text=item, **self.label_config)
            label.pack()
