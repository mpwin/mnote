import argparse
import tkinter as tk


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
    # args: argparse.Namespace = parse_args()

    root = tk.Tk()
    root.title("mnote")
    root.mainloop()


if __name__ == "__main__":
    main()
