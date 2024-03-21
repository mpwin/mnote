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

        body: tk.Text = tk.Text(
            self,
            bd=0,
            bg='#1e1e1e',
            fg='#d4d4d4',
            font=('Consolas', 16),
            padx=40,
            pady=20,
            height=20,
            width=60,
            wrap='word',
            )
        body.insert(tk.END, data['text'])
        body.config(state='disabled')
        body.pack()
        self.pack(side='left')
