import tkinter as tk


class BaseWidget(tk.Frame):
    """The base class for the different types of Mnote widgets."""

    def __init__(self, parent, data: dict) -> None:
        super().__init__(parent)
        self.data = data

    @property
    def widget_config(self) -> dict:
        return self.data.get('config', {})

    @property
    def background(self) -> str:
        return self.widget_config.get('background', '#1e1e1e')

    @property
    def foreground(self) -> str:
        return self.widget_config.get('foreground', '#d4d4d4')

    @property
    def font(self) -> str:
        return self.widget_config.get('font', 'Consolas')

    @property
    def font_size(self) -> int:
        return self.widget_config.get('font_size', 16)

    @property
    def pack_config(self) -> dict:
        return {
            'side': self.data.get('pack_side', 'left'),
            }
