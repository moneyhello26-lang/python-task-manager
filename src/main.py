"""Command-line entry point for the task manager."""

import argparse
from pathlib import Path

from src.core import (add_task, complete_task, delete_task, list_tasks,
                      load_tasks, save_tasks, search_tasks)

APP_TITLE = "Планировщик задач Python"
DEFAULT_DATA = Path.home() / ".python-task-manager.json"


def run_menu(data_path: Path) -> int:
    while True:
        print("\n1. Список задач\n2. Добавить задачу\n0. Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "0":
            return 0
        if choice == "1":
            print("\n".join(list_tasks(load_tasks(data_path))) or "Задач пока нет")
        elif choice == "2":
            title = input("Название задачи: ").strip()
            if not title:
                print("Название не может быть пустым")
                continue
            tasks = load_tasks(data_path)
            task = add_task(tasks, title)
            save_tasks(tasks, data_path)
            print(f"Добавлена задача {task['id']}")
        else:
            print("Нет такого пункта меню")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=APP_TITLE)
    parser.add_argument("command", choices=["add", "list", "menu", "search", "complete", "delete"])
    parser.add_argument("title", nargs="?")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args(argv)
    if args.command == "menu":
        return run_menu(args.data)
    tasks = load_tasks(args.data)
    if args.command == "add":
        if not args.title:
            parser.error("для add укажите название задачи")
        try:
            task = add_task(tasks, args.title)
        except ValueError as error:
            parser.error(str(error))
        save_tasks(tasks, args.data)
        print(f"Добавлена задача {task['id']}: {task['title']}")
    elif args.command in {"complete", "delete"}:
        try:
            task_id = int(args.title or "")
        except ValueError:
            parser.error("укажите числовой номер задачи")
        operation = complete_task if args.command == "complete" else delete_task
        if not operation(tasks, task_id):
            print(f"Задача {task_id} не найдена")
            return 1
        save_tasks(tasks, args.data)
        print(f"Задача {task_id} {'выполнена' if args.command == 'complete' else 'удалена'}")
    elif args.command == "search":
        if not args.title:
            parser.error("для search укажите текст поиска")
        print("\n".join(list_tasks(search_tasks(tasks, args.title))) or "Совпадений нет")
    else:
        print("\n".join(list_tasks(tasks)) or "Задач пока нет")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
