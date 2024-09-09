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

        sample_size: int = min(10, len(data['items']))
        sample: list = random.sample(data['items'], sample_size)
        self.display_items(sample)

    @property
    def label_config(self) -> dict:
        return {
            'bg': '#1e1e1e',
            'fg': '#d4d4d4',
            'font': ('Consolas', 16),
            'pady': 4,
            }

    def display_items(self, items: list) -> None:
        for item in items:
            label: tk.Label = tk.Label(text=item, **self.label_config)
            label.pack()
