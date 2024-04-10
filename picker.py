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


def get_mnotes(path: str) -> list[str]:
    if os.path.isfile(path) and path.endswith('.mnote'):
        return [path]
    else:
        return find_mnotes(path)


def find_mnotes(path: str) -> list[str]:
    """Searches for files with an '.mnote' extension.

    Args:
        path: The root directory path from where the search begins.

    Returns:
        list[str]: A list of paths to files that end with an '.mnote'
            extension.
    """
    mnotes: list[str] = []
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.mnote'):
                mnotes.append(os.path.join(dirpath, filename))
    return mnotes


def main() -> None:
    args: argparse.Namespace = parse_args()
    mnotes: list[str] = get_mnotes(args.path)
    print(random.choice(mnotes))


if __name__ == '__main__':
    main()
