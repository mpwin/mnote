import tkinter as tk


class TextWidget(tk.Frame):
    """Widget for displaying text."""

    def __init__(self, parent, data: dict) -> None:
        """Initializes a new TextWidget instance.

        Args:
            parent: Parent widget.
            data: Configuration and content for the widget.
        """
        super().__init__(parent)

        text: tk.Text = tk.Text(self)
        text.insert(tk.END, data['text'])
        text.config(**self.config(data))

        text.pack()
        self.pack(padx=40, pady=40, side='left')

    def config(self, data: dict) -> dict:
        """Configures the widget."""

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
