"""
Работа с CLI
"""

import sys

from src.TodoJournal import TodoJournal


def parse_args(_cli_args):
    """
    Обработка аргументов командной строки
    Args:
        _cli_args:

    Returns:

    """
    return []


def run(_args):
    """
    Вызываем соответствующие функции
    Args:
        _args:

    Returns:

    """
    return None


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
