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
    entries = todo.entries
    name = todo.name

    assert entries == expected_entries
    assert name == expected_name
