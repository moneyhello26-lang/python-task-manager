"""Tests for the initial task manager."""

import tempfile
import unittest
from pathlib import Path

from src.core import add_task, complete_task, list_tasks, load_tasks, save_tasks, search_tasks


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

    def test_reject_blank_or_long_title(self):
        for title in ["   ", "x" * 121]:
            with self.subTest(title=title):
                with self.assertRaises(ValueError):
                    add_task([], title)

    def test_search_ignores_letter_case(self):
        tasks = []
        add_task(tasks, "Изучить Git")
        add_task(tasks, "Оформить отчёт")
        self.assertEqual(search_tasks(tasks, "git"), [tasks[0]])
        self.assertEqual(search_tasks(tasks, "  "), [])


if __name__ == "__main__":
    unittest.main()
