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

        sample_size: int = min(10, len(data.get('items', [])))
        sample: list = random.sample(data.get('items', []), sample_size)

        for item in sample:
            item_frame: tk.Frame = tk.Frame(self)
            item_frame.pack()

            for column, text in enumerate(item):
                label: tk.Label = tk.Label(
                    item_frame,
                    bg='#1e1e1e',
                    fg='#d4d4d4',
                    font=('Consolas', 16),
                    text='[···]',
                    width=20,
                    )
                label.grid(row=0, column=column)

                label.bind(
                    '<Button-1>',
                    lambda e, label=label, text=text: label.config(text=text),
                    )

        self.pack(side='left')
