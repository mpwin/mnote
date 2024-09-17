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

        self.config(
            bg='#1e1e1e',
            height=80*len(data['items'])+40,
            padx=40,
            pady=20,
            width=400,
            )

        for item in data['items']:
            item_frame: tk.Frame = tk.Frame(
                self,
                bg='#1e1e1e',
                height=80,
                )
            item_frame.pack_propagate(False)
            item_frame.pack(fill='x')

            q: str = item['q']
            a: str = item['a']

            q_label: tk.Label = tk.Label(
                item_frame,
                anchor='w',
                bg='#1e1e1e',
                fg='#569cd6',
                font=('Consolas', 16),
                text=q,
                )
            q_label.pack(fill='x')

            a_label: tk.Label = tk.Label(
                item_frame,
                anchor='w',
                bg='#1e1e1e',
                fg='#d4d4d4',
                font=('Consolas', 16),
                text="?",
                )
            a_label.pack(fill='x')
            a_label.bind(
                '<Button-1>',
                lambda e, label=a_label, text=a: label.config(text=text),
                )

        self.pack_propagate(False)
        self.pack(**self.pack_config, fill='y')
