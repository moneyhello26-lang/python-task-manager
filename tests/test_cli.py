"""Checks for the interactive menu."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.core import load_tasks
from src.main import run_menu


class MenuTests(unittest.TestCase):
    def test_add_then_exit(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.json"
            with patch("builtins.input", side_effect=["2", "Изучить Git", "0"]):
                self.assertEqual(run_menu(path), 0)
            self.assertEqual(load_tasks(path)[0]["title"], "Изучить Git")


if __name__ == "__main__":
    unittest.main()
