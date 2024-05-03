import argparse


def parse_args(args):
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     add_help=True,
                                     description='''
                      ToDoJournal App
                ----------------------------
                Здесь можно отслеживать дела,
                которые вам надо сделать
''',
                                     epilog='''
----------------------------
    Какой-то текст :D
                                     ''')
    composing = parser.add_argument_group("Writing new todos")
    composing.add_argument("text", metavar="Текст новой тудушки", nargs="*")
    standalone = parser.add_argument_group(
        "Standalone Commands",
        "После выполнения этих комант программа завершится"
    )
    standalone.add_argument(
        "--delete",
        dest="delete",
        help="Удаляет запись по индексу",
    )
    standalone.add_argument(
        "--create",
        dest="create",
        help="Создаёт пустой туду журнал"
    )
    return parser.parse_intermixed_args(args)
