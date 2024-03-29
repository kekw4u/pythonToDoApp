import json


def main():
    pass


if __name__ == '__main__':
    main()


def create_todo_list(path_todo, todo_name):
    with open(path_todo, "w") as todo_file:
        json.dump(
            {"name": todo_name},
            todo_file,
            sort_keys=True,
            indent=4,
        )
