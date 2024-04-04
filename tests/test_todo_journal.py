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
