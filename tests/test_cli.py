"""Checks for the interactive menu."""

import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from src.core import load_tasks
from src.main import main, run_menu


class MenuTests(unittest.TestCase):
    def test_add_then_exit(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.json"
            with patch("builtins.input", side_effect=["2", "Изучить Git", "0"]):
                self.assertEqual(run_menu(path), 0)
            self.assertEqual(load_tasks(path)[0]["title"], "Изучить Git")

    def test_search_command(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.json"
            output = StringIO()
            with redirect_stdout(output):
                main(["add", "Проверить Git", "--data", str(path)])
                main(["search", "git", "--data", str(path)])
            self.assertIn("1. [ ] Проверить Git", output.getvalue())

    def test_complete_and_delete_commands(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.json"
            with redirect_stdout(StringIO()):
                main(["add", "Написать тест", "--data", str(path)])
                self.assertEqual(main(["complete", "1", "--data", str(path)]), 0)
                self.assertTrue(load_tasks(path)[0]["done"])
                self.assertEqual(main(["delete", "1", "--data", str(path)]), 0)
            self.assertEqual(load_tasks(path), [])


if __name__ == "__main__":
    unittest.main()
