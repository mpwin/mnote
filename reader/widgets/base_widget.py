import tkinter as tk


class BaseWidget(tk.Frame):
    """The base class for the different types of Mnote widgets."""

    def __init__(self, parent, data: dict) -> None:
        super().__init__(parent)
        self.data = data

    @property
    def pack_config(self) -> dict:
        return {
            'side': self.data.get('pack_side', 'left'),
            }
