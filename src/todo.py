from src.TodoJournal import TodoJournal


def run(args):
    todo = TodoJournal("../tests/data/test_todo")
    if args.text:
        raw_text = ''.join(args.text)
        todo.add_entry(raw_text)
    if args.delete:
        todo.remove_entry(int(args.delete))
