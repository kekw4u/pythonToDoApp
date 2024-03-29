"""                 Приложение ToDoList

Todo:
    * Сюда пишем то, что надо сделать в последующем

"""

import json


def main() -> None:
    """
    Returns:
        None: Ничего не возвращаем
    """
    print("Hello, World!")


if __name__ == '__main__':
    main()


class TodoJournal:
    """
    Класс ToDoListJournal

    Attributes:
        path_todo(str): Путь до файла с туду листом
        name(str): Название туду листа
    """

    def __init__(self, path_todo: str, name: str):
        """Конструктор класса: создаёт объект с заданными аттрибутами

        Args:
            path_todo(str): Путь до файла с туду листом
            name(str): Название туду листа

        Returns:
        """
        self.path_todo = path_todo
        self.name = name

    def create(self) -> None:
        """Создаёт файл с заданными json-параметрами"""
        with open(self.path_todo, "w", encoding='utf-8') as todo_file:
            json.dump(
                {"name": self.name, "todos": []},
                todo_file,
                sort_keys=True,
                indent=4,
                ensure_ascii=False,
            )

    def add_entry(self, new_entry) -> None:
        """Добавляет новую тудушку в существующий туду лист

        Args:
            new_entry(str): Туду, который будет добавлен

        Returns:

        """
        data = self._parse()

        name = data["name"]
        todos = data["todos"]

        todos.append(new_entry)

        new_data = {
            "name": name,
            "todos": todos,
        }

        self._update(new_data)

    def remove_entry(self, index: int) -> None:
        """Удаляет тудушку с заданным индексом

        Args:
            index(int): Номер тудушки, которая будет удалена

        Returns:

        """
        data = self._parse()
        name = data["name"]
        todos = data["todos"]

        todos.remove(todos[index])

        new_data = {
            "name": name,
            "todos": todos,
        }

        self._update(new_data)

    def _update(self, new_data: dict) -> None:
        """Обновляет туду лист, записывая туда данные из словаря new_data

        Args:
            new_data(dict): Список Тудушек

        Returns:

        """
        with open(self.path_todo, "w", encoding='utf-8') as todo_file:
            json.dump(
                new_data,
                todo_file,
                sort_keys=True,
                indent=4,
                ensure_ascii=False,
            )

    def _parse(self) -> dict:
        """Получает данные из туду листа

        Returns:
            dict: Данные, полученные из файла(Туду листа)
        """
        with open(self.path_todo, 'r', encoding='utf-8') as todo_file:
            data = json.load(todo_file)
        return data
