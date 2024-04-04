"""                 Приложение ToDoList
"""

import json
import sys


class ToDoNotFoundError(Exception):
    """
    Класс Ошибки индексирования
    """
    pass


class TodoJournal:
    """
    Класс ToDoListJournal

    Attributes:
        path_todo(str): Путь до файла с туду листом
        name(str): Название туду листа
    """

    shortcut_names = {"first": 0, "last": -1}

    def __init__(self, path_todo: str):
        """Конструктор класса: создаёт объект с заданными аттрибутами

        Args:
            path_todo(str): Путь до файла с туду листом
        """
        self.path_todo = path_todo
        todo_data = self._parse()
        self.name = todo_data['name']
        self.entries = todo_data['todos']

    @staticmethod
    def create(filename, name) -> None:
        """Создаёт файл с заданными json-параметрами"""
        try:
            with open(filename, "w", encoding='utf-8') as todo_file:
                json.dump(
                    {"name": name, "todos": []},
                    todo_file,
                    sort_keys=True,
                    indent=4,
                    ensure_ascii=False,
                )
        except FileNotFoundError:
            print(f"Данный путь некорректен: {filename}")
            sys.exit(1)
        except PermissionError:
            print(f"У вас нет прав на запись этого файла: {filename}")
            sys.exit(1)

    def add_entry(self, new_entry: str) -> None:
        """Добавляет новую тудушку в существующий туду лист

        Args:
            new_entry(str): Туду, который будет добавлен

        """
        self.entries.append(new_entry)
        new_data = {
            "name": self.name,
            "todos": self.entries,
        }
        self._update(new_data)

    def remove_entry(self, index: int) -> None:
        """Удаляет тудушку с заданным индексом

        Args:
            index(int): Номер тудушки, которая будет удалена
        """
        try:
            del self.entries[index]
        except (IndexError, TypeError):
            print("Туду с заданным индексом не существует!")
            return
        new_data = {
            "name": self.name,
            "todos": self.entries,
        }
        self._update(new_data)

    def _update(self, new_data: dict) -> None:
        """Обновляет туду лист, записывая туда данные из словаря new_data

        Args:
            new_data(dict): Список Тудушек
        """
        try:
            with open(self.path_todo, "w", encoding='utf-8') as todo_file:
                json.dump(
                    new_data,
                    todo_file,
                    sort_keys=True,
                    indent=4,
                    ensure_ascii=False,
                )

        except FileNotFoundError:
            print(f"Данный путь некорректен: {self.path_todo}")
            sys.exit(1)
        except PermissionError:
            print(f"У вас нет прав на запись этого файла: {self.path_todo}")
            sys.exit(1)

    def _parse(self) -> list:
        """Получает данные из туду листа

        Returns:
            list: Данные, полученные из файла(Туду листа)
        """
        try:
            with open(self.path_todo, 'r', encoding='utf-8') as todo_file:
                data = json.load(todo_file)
            return data
        except FileNotFoundError:
            print(f"Данный путь некорректен: {self.path_todo}")
            sys.exit(1)
        except PermissionError:
            print(f"У вас нет прав на чтение этого файла: {self.path_todo}")
            sys.exit(1)

    def __setattr__(self, name, value):
        error_msg = ''
        if name in self.shortcut_names:
            error_msg = f"readonly attribute {name}"
        if error_msg:
            raise AttributeError(error_msg)
        super().__setattr__(name, value)

    def __len__(self):
        return len(self.entries)

    def __getitem__(self, item):
        try:
            return self.entries[item]
        except (TypeError, IndexError) as error:
            raise ToDoNotFoundError("Туду с таким индексом не существует!") from error

    def __getattr__(self, item):
        index = self.shortcut_names.get(item)
        if index is not None:
            return self.entries[index]

        cls = type(self)
        raise AttributeError(f"{cls.__name__}-объект не имеет поля {item}")

    def __iter__(self):
        return iter(self.entries)

    def __next__(self):
        return next(self)
