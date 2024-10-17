import tkinter as tk


class BaseWidget(tk.Frame):
    """The base class for the different types of Mnote widgets."""

    def __init__(self, parent, data: dict) -> None:
        super().__init__(parent)
        self.data = data

    @property
    def frame_config(self) -> dict:
        return {
            'bg': self.background,
            'padx': 40,
            'pady': 40,
            }

    @property
    def widget_config(self) -> dict:
        return self.data.get('config', {})

    @property
    def background(self) -> str:
        return self.widget_config.get('background', '#1e1e1e')

    @property
    def font(self) -> str:
        return self.widget_config.get('font', 'Consolas')

    @property
    def font_color(self) -> str:
        return self.widget_config.get('font_color', '#d4d4d4')

    @property
    def font_size(self) -> int:
        return self.widget_config.get('font_size', 16)

    @property
    def highlight_color(self) -> str:
        return self.widget_config.get('highlight_color', '#569cd6')

    @property
    def pack_config(self) -> dict:
        return {
            'expand': True,
            'fill': 'both',
            'side': self.data.get('pack_side', 'left'),
            }
