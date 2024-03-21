import tkinter as tk


class Panel(tk.Frame):
    """The base class for the different types of Mnote panels.

    Attributes:
        app: A reference to the main Mnote App instance.
        data: A dict containing configuration and content for the panel.
    """

    def __init__(self, app: 'App', data: dict) -> None:
        """Initializes a new Panel instance.

        Args:
            app: The main Mnote App instance.
            data: Configuration and content for the panel.
        """
        super().__init__(app)
        self.app: 'App' = app
        self.data: dict = data
