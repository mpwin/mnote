import tkinter as tk


class BasePanel(tk.Frame):
    """The base class for the different types of Mnote panels.

    Attributes:
        data: A dict containing configuration and content for the panel.
    """

    def __init__(self, data: dict) -> None:
        """Initializes a new BasePanel instance.

        Args:
            data: Configuration and content for the panel.
        """
        super().__init__()
        self.data: dict = data
