import argparse
import os
import random


def parse_args() -> argparse.Namespace:
    """Parses command-line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('path')
    return parser.parse_args()


def find_mnotes(path: str) -> list[str]:
    """Searches for directories with an '.mnote' extension.

    Args:
        path: The root directory path from which the search begins.

    Returns:
        list[str]: A list of paths to directories that end with an '.mnote'
            extension.
    """
    mnotes: list[str] = []
    for dirpath, dirnames, _ in os.walk(path):
        for dirname in dirnames:
            if dirname.endswith('.mnote'):
                mnotes.append(os.path.join(dirpath, dirname))
    return mnotes


def main() -> None:
    args: argparse.Namespace = parse_args()

    if args.path.endswith('.mnote'):
        print(args.path)
    else:
        mnotes: list[str] = find_mnotes(args.path)
        print(random.choice(mnotes))


if __name__ == '__main__':
    main()
