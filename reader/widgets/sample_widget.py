import random
import tkinter as tk


class SampleWidget(tk.Frame):
    """Widget for listing a random sample from a larger list of items."""

    def __init__(self, parent, data: dict) -> None:
        """Initializes a new SampleWidget instance.

        Args:
            parent: Parent widget.
            data: Configuration and content for the widget.
        """
        super().__init__(parent)
        self.data = data

        sample: list = random.sample(self.data['items'], self.sample_size)
        self.display_items(sample)

        self.config(self.frame_config)
        self.pack(side='left')

    @property
    def frame_config(self) -> dict:
        return {
            'bg': '#1e1e1e',
            'padx': 40,
            'pady': 40,
            }

    @property
    def label_config(self) -> dict:
        return {
            'bg': '#1e1e1e',
            'fg': '#d4d4d4',
            'font': ('Consolas', 16),
            'pady': 4,
            }

    @property
    def sample_size(self) -> int:
        return min(self.data.get('sample_size', 10), len(self.data['items']))

    def display_items(self, items: list) -> None:
        for item in items:
            label: tk.Label = tk.Label(self, text=item, **self.label_config)
            label.pack()
