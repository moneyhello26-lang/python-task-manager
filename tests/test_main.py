"""Tests for the initial task manager."""

import tempfile
import unittest
from pathlib import Path

from src.core import add_task, complete_task, list_tasks, load_tasks, save_tasks


class TaskTests(unittest.TestCase):
    def test_add_save_and_load(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.json"
            tasks = []
            add_task(tasks, "Подготовить отчёт")
            save_tasks(tasks, path)
            self.assertEqual(load_tasks(path), tasks)
            self.assertEqual(list_tasks(tasks), ["1. [ ] Подготовить отчёт"])

    def test_complete_task(self):
        tasks = []
        add_task(tasks, "Проверить ветку")
        self.assertTrue(complete_task(tasks, 1))
        self.assertEqual(list_tasks(tasks), ["1. [x] Проверить ветку"])
        self.assertFalse(complete_task(tasks, 99))


if __name__ == "__main__":
    unittest.main()
