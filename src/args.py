import argparse


def parse_args(args):
    parser = argparse.ArgumentParser()
    composing = parser.add_argument_group("Writing new todos",
                                "чтобы добавить новую запись в туду лист"
                                        "необходимо выполнить X")
    composing.add_argument("text", metavar="", nargs="")
    standalone = parser.add_argument_group(
        "Standaline Commands",
        "После выполнения этих комант программа завершится"
    )
    standalone.add_argument(
        "--delete",
        dest="delete",
        help="Удаляет запись по индексу",
    )
    return parser.parse_intermixed_args(args)
