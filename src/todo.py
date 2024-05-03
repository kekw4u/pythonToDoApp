import os
import re

import conf
from conf import PATH
from src.TodoJournal import TodoJournal


def run(args):
    regex = re.compile(r"^[^/]+$")
    todo = TodoJournal(conf.PATH)
    if args.text:
        raw_text = ' '.join(args.text)
        todo.add_entry(raw_text)
    if args.delete:
        print(f"{todo[int(args.delete)]}\n")
        print("Вы уверены, что хотите удалить эту запись: y/n")
        answer = str(input())
        if answer == 'y':
            todo.remove_entry(int(args.delete))
    if args.create:
        if not regex.match(args.create):
            print("Неверное название файла")
            return
        if os.path.exists("tests/data/"+args.create):
            print("Такой туду журнал уже существует")
            return
        TodoJournal.create("tests/data/"+args.create, args.create)
