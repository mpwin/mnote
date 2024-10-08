import tkinter as tk
from pathlib import Path

from .widgets.image_widget import ImageWidget
from .widgets.link_widget import LinkWidget
from .widgets.recall_sample_widget import RecallSampleWidget
from .widgets.recall_widget import RecallWidget
from .widgets.sample_widget import SampleWidget
from .widgets.text_widget import TextWidget


class App(tk.Tk):
    """A Tkinter application for displaying Mnote content."""

    def __init__(self, mnote_path: str, data: dict) -> None:
        """Initializes the App object based on its data argument.

        Args:
            mnote_path: The file system location of the Mnote.
            data: The deserialized data from the Mnote's YAML file.
        """
        super().__init__()
        self.mnote_path: Path = Path(mnote_path)
        self.mnote_name: str = self.mnote_path.stem
        self.mnote_directory: Path = self.mnote_path.parent

        self.widgets: list = []
        self.title("mnote")
        self.config(bg='#1e1e1e')

        if 'header' in data:
            self.header = self.make_header(data['header'])
        for widget in data.get('widgets', []):
            match widget['type']:
                case 'image':
                    self.widgets.append(
                        ImageWidget(self, widget, self.mnote_directory)
                        )
                case 'link':
                    self.widgets.append(LinkWidget(self, widget))
                case 'recall':
                    self.widgets.append(RecallWidget(self, widget))
                case 'recall sample':
                    self.widgets.append(RecallSampleWidget(self, widget))
                case 'sample':
                    self.widgets.append(SampleWidget(self, widget))
                case 'text':
                    self.widgets.append(TextWidget(self, widget))

    def make_header(self, text: str) -> tk.Label:
        """Creates and displays a header label with the specified text.

        Args:
            text: The text to be displayed in the header label.

        Returns:
            The header tkinter.Label object.
        """
        header: tk.Label = tk.Label(
            self,
            bg='#2d2d2d',
            fg='#ffffff',
            font=('Consolas', 16),
            padx=8,
            pady=4,
            text=text,
            )
        header.pack(fill='both')
        return header
