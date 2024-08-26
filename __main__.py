import argparse

from picker import pick
from reader import read


def parse_args() -> argparse.Namespace:
    """Parses command-line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('path')
    return parser.parse_args()


if __name__ == "__main__":
    args: argparse.Namespace = parse_args()
    read(pick(args.path))
