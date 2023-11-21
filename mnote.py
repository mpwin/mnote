import argparse
import tkinter as tk
import yaml


def parse_args() -> argparse.Namespace:
    """
    Parses command-line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    return parser.parse_args()


def main():
    args: argparse.Namespace = parse_args()

    with open(args.path) as f:
        data: dict = yaml.safe_load(f)

    root = tk.Tk()
    root.title("mnote")

    note: tk.Label = tk.Label(
        root,
        justify='left',
        text=data['body'],
        wraplength=400,
        )
    note.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
