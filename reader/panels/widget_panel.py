import tkinter as tk


class WidgetPanel(tk.Frame):
    def __init__(self, data: dict) -> None:
        super().__init__()

        for widget in data['widgets']:
            for item in widget['items']:
                item_frame: tk.Frame = tk.Frame(
                    self,
                    bg='#1e1e1e',
                    )
                item_frame.pack(fill='x')

                l, r = item

                l_label: tk.Label = tk.Label(
                    item_frame,
                    bg='#1e1e1e',
                    fg='#d4d4d4',
                    font=('Consolas', 16),
                    text="Recall",
                    width=20,
                    )
                l_label.grid(row=0, column=0)
                l_label.bind(
                    '<Button-1>',
                    lambda e, label=l_label, text=l:
                        self.on_label_click(label, text)
                    )
                r_label: tk.Label = tk.Label(
                    item_frame,
                    bg='#1e1e1e',
                    fg='#d4d4d4',
                    font=('Consolas', 16),
                    text="Recall",
                    width=20,
                    )
                r_label.grid(row=0, column=1)
                r_label.bind(
                    '<Button-1>',
                    lambda e, label=r_label, text=r:
                        self.on_label_click(label, text)
                    )

        self.pack()

    def on_label_click(self, label, text):
        label.config(text=text)
