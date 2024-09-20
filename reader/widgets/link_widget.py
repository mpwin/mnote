import tkinter as tk
import webbrowser

from .base_widget import BaseWidget


class LinkWidget(BaseWidget):
    """Widget for displaying a clickable link to a url."""

    def __init__(self, parent, data: dict) -> None:
        """Initializes a new LinkWidget instance.

        Args:
            parent: Parent widget.
            data: Configuration and content for the widget.
        """
        super().__init__(parent, data)

        label: tk.Label = tk.Label(
            self,
            text=self.data['text'],
            **self.label_config,
            )
        label.bind(
            '<Button-1>',
            lambda e: self.open_link(self.data['url']),
            )
        label.pack()

        self.config(self.frame_config)
        self.pack(self.pack_config)

    @property
    def close(self) -> bool:
        return self.data.get('close', False)

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
            'fg': '#0e639c',
            'font': (self.font, self.font_size),
            'pady': 4,
            }

    def open_link(self, url: str) -> None:
        webbrowser.open_new(url)

        if self.close:
            self.winfo_toplevel().destroy()
