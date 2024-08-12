import tkinter as tk

from ..widgets.recall_sample_widget import RecallSampleWidget


class WidgetPanel(tk.Frame):
    def __init__(self, parent, data: dict) -> None:
        super().__init__(parent)

        self.widgets: list = []

        for widget in data.get('widgets', []):
            if widget['type'] == 'recall sample':
                self.widgets.append(RecallSampleWidget(self, widget))

        self.pack()
