import tkinter as tk


class Text():
    """A wrapper for the Tkinter Text widget."""

    default_config: dict = {
        'bd': 0,
        'state': 'disabled',
        'wrap': 'word',
        }

    def __init__(self, text: str, config: dict = {}) -> None:
        """Initializes a new Text component instance."""
        self._text: str = text
        self._config: dict = {**self.default_config, **config}

    def __len__(self) -> int:
        return len(self._text)

    def __getitem__(self, index: int) -> str:
        return self._text[index]

    @property
    def config(self) -> dict:
        return {
            **self._config,
            'height': self.height,
            'width': self.width,
            }

    @property
    def height(self) -> int:
        return len(self.text.splitlines())

    @property
    def text(self) -> str:
        return self._text

    @property
    def width(self) -> int:
        return max(len(line) for line in self.text.splitlines())

    def pack(self, parent: tk.Widget) -> None:
        self._widget: tk.Text = tk.Text(parent)
        self._widget.insert(tk.END, self.text)
        self._widget.config(self.config)
        self._widget.pack(expand=True, fill='both')
