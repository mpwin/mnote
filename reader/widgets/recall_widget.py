import tkinter as tk

from .base_widget import BaseWidget


class RecallWidget(BaseWidget):
    """Widget for displaying recall items."""

    def __init__(self, parent, data: dict) -> None:
        """Initializes a new RecallWidget instance.

        Args:
            parent: Parent widget.
            data: Configuration and content for the widget.
        """
        super().__init__(parent, data)

        self.display_items(self.data['items'])

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
            'anchor': 'w',
            'bg': self.background,
            'font': (self.font, self.font_size),
            'width': 40,
            }

    def display_items(self, items: list) -> None:
        for item in items:
            item_frame: tk.Frame = tk.Frame(self)
            item_frame.pack(pady=(0, 20))

            q_label: tk.Label = tk.Label(
                item_frame,
                fg='#569cd6',
                text=item['q'],
                **self.label_config,
                )
            q_label.pack()

            a_label: tk.Label = tk.Label(
                item_frame,
                fg=self.font_color,
                text="?",
                **self.label_config,
                )
            a_label.pack()

            a_label.bind(
                '<Button-1>',
                lambda e, label=a_label, text=item['a']:
                    label.config(text=text),
                )
