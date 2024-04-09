"""
Скрипт для тестирования ToDoJournal'а
"""
import json

import pytest

from src.TodoJournal import TodoJournal


def test_init() -> None:
    """
    Функция тестирования TodoJournal'а
    """
    test_create_journal_validpath("data/")
    test_add_entry("data/")
    test_len_method_empty_journal("data/")
    test_len_method_two_entries_journal("data/")
    test_create_journal_wrongpath("wrong/path/todo/")
    test_create_journal_permissionerror("data/")


def test_create_journal_validpath(tmpdir):
    todo_filename = "test_todo"
    todo = tmpdir + todo_filename

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
    todo = tmpdir + todo_filename

    expected_todo = json.dumps(
        {
            "name": "test",
            "todos": ["Сходить за молоком"]
        },
        indent=4,
        ensure_ascii=False, )

    TodoJournal.create(todo, "test")
    todo_jrnl = TodoJournal(todo)
    todo_jrnl.add_entry("Сходить за молоком")
    with open(todo, 'r', encoding='utf-8') as todoFile:
        data = todoFile.read()
    assert expected_todo == data


def test_len_method_empty_journal(tmpdir):
    todo_filename = "test_todo"
    todo = tmpdir + todo_filename

    expected_len = 0
    TodoJournal.create(todo, "test")
    todo_jrnl = TodoJournal(todo)
    count_of_entries = len(todo_jrnl)
    assert expected_len == count_of_entries


def test_len_method_two_entries_journal(tmpdir):
    todo_filename = "test_todo"
    todo = tmpdir + todo_filename

    expected_len = 2
    TodoJournal.create(todo, "test")
    todo_jrnl = TodoJournal(todo)
    todo_jrnl.add_entry("Бег 5 км")
    todo_jrnl.add_entry("Тесты по питону")
    count_of_entries = len(todo_jrnl)
    assert expected_len == count_of_entries


def test_create_journal_wrongpath(tmpdir):
    todo_filename = "test_todo"
    todo = tmpdir + todo_filename

    with pytest.raises(FileNotFoundError):
        TodoJournal.create(todo, "wrong_path")


def test_create_journal_permissionerror(tmpdir):
    todo_filename = "permission_error_file"
    todo = tmpdir + todo_filename

    with pytest.raises(PermissionError):
        TodoJournal.create(todo, "permissionError")
