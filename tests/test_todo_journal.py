"""
Скрипт для тестирования ToDoJournal'а
"""
from src.TodoJournal import TodoJournal


def test_init() -> None:
    """
    Функция тестирования TodoJournal'а
    """
    expected_entries = []
    expected_name = "test_todo"

    todo = TodoJournal("data/test_todo")
    todo.add_entry("ads")
    entries = todo.entries
    name = todo.name

    print(todo.first)
    print(todo.first)
    print(todo[0])

    assert entries == expected_entries
    assert name == expected_name
