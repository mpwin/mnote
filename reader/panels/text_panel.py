import tkinter as tk

from .base_panel import BasePanel


class TextPanel(BasePanel):
    """A subclass of BasePanel specialized for displaying text."""

    def __init__(self, app: 'App', data: dict) -> None:
        """Initializes a new TextPanel instance.

        Args:
            app: The main Mnote App instance.
            data: Configuration and content for the panel.
        """
        super().__init__(app, data)

        text: tk.Text = tk.Text(self)
        text.insert(tk.END, data['text'])
        text.config(**self.config(data))

        text.pack()
        self.pack(padx=40, pady=40, side='left')

    def config(self, data: dict) -> dict:
        """Configures the text widget used within the TextPanel."""

        def height(text: str) -> int:
            return len(text.split('\n'))

        def width(text: str) -> int:
            line_lengths = [len(line) for line in text.split('\n')]
            return max(line_lengths)

        return {
            'bd': 0,
            'bg': '#1e1e1e',
            'fg': '#d4d4d4',
            'font': ('Consolas', 16),
            'height': height(data['text']),
            'state': 'disabled',
            'width': width(data['text']),
            'wrap': 'word',
            }
