import json


def main():
    pass


if __name__ == '__main__':
    main()


def create_todo_list(path_todo, todo_name):
    with open(path_todo, "w", encoding='utf-8') as todo_file:
        json.dump(
            {"name": todo_name},
            todo_file,
            sort_keys=True,
            indent=4,
        )


def add_todo(path_todo, new_todo):
    data = parse_todo(path_todo)
    name = data["name"]
    todos = data["todos"]

    todos.append(new_todo)

    new_data = {
        "name": name,
        "todos": todos,
    }

    update_todo(path_todo, new_data)


def remove_todo(path_todo, index):
    data = parse_todo(path_todo)
    name = data["name"]
    todos = data["todos"]

    todos.remove(todos[index])

    new_data = {
        "name": name,
        "todos": todos,
    }

    update_todo(path_todo, new_data)


def update_todo(path_todo, new_data):
    with open(path_todo, "w", encoding='utf-8') as todo_file:
        json.dump(
            new_data,
            todo_file,
            sort_keys=True,
            indent=4,
            ensure_ascii=False,
        )


def parse_todo(path_todo):
    with open(path_todo, 'r') as todo_file:
        data = json.load(todo_file)
    return data