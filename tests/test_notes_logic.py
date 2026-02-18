import unittest
from modules.notes_manager import NotesManager


class TestNotesManager(unittest.TestCase):

    def setUp(self):
        self.manager = NotesManager()
        self.manager.notes = []

    def test_generate_id_empty(self):
        self.assertEqual(self.manager.generate_id(), 1)

    def test_generate_id_with_existing(self):
        self.manager.notes = [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ]
        self.assertEqual(self.manager.generate_id(), 4)


if __name__ == "__main__":
    unittest.main()
