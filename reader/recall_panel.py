import tkinter as tk

from .panel import Panel


class RecallPanel(Panel):
    """A subclass of Panel specialized for displaying recall items."""

    def __init__(self, app: 'App', data: dict) -> None:
        """Initializes a new RecallPanel instance.

        Args:
            app: The main Mnote App instance.
            data: Configuration and content for the panel.
        """
        super().__init__(app, data)

        self.config(
            bg='#1e1e1e',
            height=80*len(data['items'])+40,
            padx=40,
            pady=20,
            width=400,
            )

        for item in data['items']:
            item_frame: tk.Frame = tk.Frame(
                self,
                bg='#1e1e1e',
                height=80,
                )
            item_frame.pack_propagate(False)
            item_frame.pack(fill='x')

            q: str = item['q']
            a: str = item['a']

            q_label: tk.Label = tk.Label(
                item_frame,
                anchor='w',
                bg='#1e1e1e',
                fg='#569cd6',
                font=('Consolas', 16),
                text=q,
                )
            q_label.pack(fill='x')

            a_label: tk.Label = tk.Label(
                item_frame,
                anchor='w',
                bg='#1e1e1e',
                fg='#d4d4d4',
                font=('Consolas', 16),
                text=a,
                )

            button: tk.Button = tk.Button(
                item_frame,
                activebackground='#569cd6',
                activeforeground='#d4d4d4',
                bg='#1e1e1e',
                fg='#d4d4d4',
                font=('Consolas', 12),
                text="Recall",
                )
            button.config(
                command=lambda label=a_label, text=a, button=button: (
                    label.pack(fill='x'),
                    button.pack_forget(),
                    )
                )
            button.pack(fill='x')

        self.pack_propagate(False)
        self.pack(fill='y', side='left')
