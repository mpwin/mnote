import os
import random


def pick(path: str) -> str:
    mnotes: list[str] = get_mnotes(path)
    return(random.choice(mnotes))


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
