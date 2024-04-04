"""
Скрипт для тестирования ToDoJournal'а
"""
import json

from src.TodoJournal import TodoJournal


def test_init() -> None:
    """
    Функция тестирования TodoJournal'а
    """
    test_create_journal("data/")
    test_add_entry("data/")


def test_create_journal(tmpdir):
    todo_filename = "test_todo"
    todo = tmpdir+todo_filename

    expected_todo = json.dumps(
        {
            "name": "test",
            "todos": []
        },
        indent=4)

    TodoJournal.create(todo, "test")
    with open(todo, 'r', encoding='utf-8') as todoFile:
        data = todoFile.read()
    assert expected_todo == data


def test_add_entry(tmpdir):
    todo_filename = "test_todo"
    todo = tmpdir+todo_filename

    expected_todo = json.dumps(
        {
        "name": "test",
        "todos": ["Сходить за молоком"]
        },
        indent=4,
        ensure_ascii=False,)

    TodoJournal.create(todo, "test")
    todo_jrnl = TodoJournal(todo)
    todo_jrnl.add_entry("Сходить за молоком")
    with open(todo, 'r', encoding='utf-8') as todoFile:
        data = todoFile.read()
    assert expected_todo == data
