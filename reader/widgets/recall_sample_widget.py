import random
import tkinter as tk

from .base_widget import BaseWidget


class RecallSampleWidget(BaseWidget):
    """Widget for listing a random sample of recall items from a larger list."""

    def __init__(self, parent, data: dict) -> None:
        """Initializes a new RecallSampleWidget instance.

        Args:
            parent: Parent widget.
            data: Content for the widget.
        """
        super().__init__(parent, data)

        sample: list = random.sample(self.data['items'], self.sample_size)
        self.display_items(sample)

        self.config(self.frame_config)
        self.pack(self.pack_config)

    @property
    def frame_config(self) -> dict:
        return {
            'bg': self.background,
            'padx': 40,
            'pady': 40,
            }

    @property
    def label_config(self) -> dict:
        return {
            'bg': self.background,
            'fg': self.font_color,
            'font': (self.font, self.font_size),
            'text': "?",
            'width': 40,
            }

    @property
    def sample_size(self) -> int:
        return min(self.data.get('sample_size', 10), len(self.data['items']))

    def display_items(self, items: list) -> None:
        def get_text(data: list | str) -> str:
            return random.choice(data) if isinstance(data, list) else data

        for item in items:
            item_frame: tk.Frame = tk.Frame(self)
            item_frame.pack()

            for column, data in enumerate(item):
                label: tk.Label = tk.Label(item_frame, **self.label_config)
                text: str = get_text(data)

                label.grid(row=0, column=column)
                label.bind(
                    '<Button-1>',
                    lambda e, label=label, text=text: label.config(text=text),
                    )
