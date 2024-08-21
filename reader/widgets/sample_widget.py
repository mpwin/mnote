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

        for item in sample:
            item_label: tk.Label = tk.Label(
                bg='#1e1e1e',
                fg='#d4d4d4',
                font=('Consolas', 16),
                pady=4,
                text=item,
                )
            item_label.pack()
