"""Tests for the initial task manager."""

import tempfile
import unittest
from pathlib import Path

from src.core import add_task, list_tasks, load_tasks, save_tasks


class TaskTests(unittest.TestCase):
    def test_add_save_and_load(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.json"
            tasks = []
            add_task(tasks, "Подготовить отчёт")
            save_tasks(tasks, path)
            self.assertEqual(load_tasks(path), tasks)
            self.assertEqual(list_tasks(tasks), ["1. [ ] Подготовить отчёт"])


if __name__ == "__main__":
    unittest.main()
