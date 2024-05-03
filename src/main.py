"""
Работа с CLI
"""

import sys

from src.args import parse_args
from src.todo import run


def main():
    """
        Работа с Командной строкой
    """
    try:
        cli_args = sys.argv[1:]
        args = parse_args(cli_args)
        return run(args)
    except Exception as error:
        print(error)
        return 1


main()
