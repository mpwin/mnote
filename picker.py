import argparse
import os
import random


def get_path_arg() -> str:
    """Parses command-line arguments to return the 'path' argument.

    Returns:
        str: The 'path' command-line argument.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('path')

    args: argparse.Namespace = parser.parse_args()
    return args.path


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
    path: str = get_path_arg()

    if path.endswith('.mnote'):
        print(path)
    else:
        mnotes: list[str] = find_mnotes(path)
        print(random.choice(mnotes))


if __name__ == '__main__':
    main()
