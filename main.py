import json
import sys


def main():
    pass


if __name__ == '__main__':
    main()


class TodoJournal:
    def __init__(self, path_todo, name):
        self.path_todo = path_todo
        self.name = name

    def create(self):
        with open(self.path_todo, "w", encoding='utf-8') as todo_file:
            json.dump(
                {"name": self.name, "todos": []},
                todo_file,
                sort_keys=True,
                indent=4,
                ensure_ascii=False,
            )

    def add_entry(self, new_entry):
        data = self._parse()

        name = data["name"]
        todos = data["todos"]

        todos.append(new_entry)

        new_data = {
            "name": name,
            "todos": todos,
        }

        self._update(new_data)

    def remove_entry(self, index):
        data = self._parse()
        name = data["name"]
        todos = data["todos"]

        todos.remove(todos[index])

        new_data = {
            "name": name,
            "todos": todos,
        }

        self._update(new_data)

    def _update(self, new_data):
        with open(self.path_todo, "w", encoding='utf-8') as todo_file:
            json.dump(
                new_data,
                todo_file,
                sort_keys=True,
                indent=4,
                ensure_ascii=False,
            )

    def _parse(self):
        with open(self.path_todo, 'r') as todo_file:
            data = json.load(todo_file)
        return data
