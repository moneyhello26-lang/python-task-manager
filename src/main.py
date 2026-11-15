"""Command-line entry point for the task manager."""

import argparse
from pathlib import Path

from src.core import add_task, list_tasks, load_tasks, save_tasks

APP_TITLE = "Менеджер задач"
DEFAULT_DATA = Path.home() / ".python-task-manager.json"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=APP_TITLE)
    parser.add_argument("command", choices=["add", "list"])
    parser.add_argument("title", nargs="?")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args(argv)
    tasks = load_tasks(args.data)
    if args.command == "add":
        if not args.title:
            parser.error("для add укажите название задачи")
        task = add_task(tasks, args.title)
        save_tasks(tasks, args.data)
        print(f"Добавлена задача {task['id']}: {task['title']}")
    else:
        print("\n".join(list_tasks(tasks)) or "Задач пока нет")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
