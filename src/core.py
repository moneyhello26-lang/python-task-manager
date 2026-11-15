"""Task storage and basic operations."""

import json
from pathlib import Path


def load_tasks(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_tasks(tasks: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(tasks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def add_task(tasks: list[dict], title: str) -> dict:
    title = title.strip()
    if not title:
        raise ValueError("Название задачи не может быть пустым")
    if len(title) > 120:
        raise ValueError("Название задачи не может быть длиннее 120 символов")
    task = {"id": max((task["id"] for task in tasks), default=0) + 1,
            "title": title, "done": False}
    tasks.append(task)
    return task


def list_tasks(tasks: list[dict]) -> list[str]:
    return [f"{task['id']}. [{'x' if task['done'] else ' '}] {task['title']}"
            for task in tasks]


def complete_task(tasks: list[dict], task_id: int) -> bool:
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def search_tasks(tasks: list[dict], query: str) -> list[dict]:
    query = query.strip().casefold()
    if not query:
        return []
    return [task for task in tasks if query in task["title"].casefold()]
