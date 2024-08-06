import tkinter as tk
from pathlib import Path

from .panels import ImagePanel, RecallPanel, SamplePanel, TextPanel


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

        self.panels: list = []
        self.title("mnote")
        self.config(bg='#1e1e1e')
        self.protocol('WM_DELETE_WINDOW', self.on_close)

        if 'header' in data:
            self.header = self.make_header(data['header'])
        for panel in data.get('panels', []):
            match panel['type']:
                case 'image':
                    self.panels.append(
                        ImagePanel(panel['data'], self.mnote_directory)
                        )
                case 'recall':
                    self.panels.append(RecallPanel(panel['data']))
                case 'sample':
                    self.panels.append(SamplePanel(panel['data']))
                case 'text':
                    self.panels.append(TextPanel(panel['data']))

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

    def on_close(self) -> None:
        """Handles the event triggered by closing the Tkinter window."""
        print(self.mnote_path)
        self.destroy()
