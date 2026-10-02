import unittest
from solution import RecordStore


class TestLevel1(unittest.TestCase):
    def setUp(self):
        self.s = RecordStore()

    def test_get_missing(self):
        self.assertIsNone(self.s.get("a", "x"))

    def test_set_then_get(self):
        self.assertIsNone(self.s.set("a", "x", "1"))
        self.assertEqual(self.s.get("a", "x"), "1")

    def test_overwrite(self):
        self.s.set("a", "x", "1")
        self.s.set("a", "x", "2")
        self.assertEqual(self.s.get("a", "x"), "2")

    def test_fields_and_keys_are_independent(self):
        self.s.set("a", "x", "1")
        self.s.set("a", "y", "2")
        self.s.set("b", "x", "3")
        self.assertEqual(self.s.get("a", "x"), "1")
        self.assertEqual(self.s.get("a", "y"), "2")
        self.assertEqual(self.s.get("b", "x"), "3")
        self.assertIsNone(self.s.get("b", "y"))

    def test_delete(self):
        self.s.set("a", "x", "1")
        self.assertTrue(self.s.delete("a", "x"))
        self.assertIsNone(self.s.get("a", "x"))
        self.assertFalse(self.s.delete("a", "x"))

    def test_delete_missing(self):
        self.assertFalse(self.s.delete("nope", "x"))
        self.s.set("a", "x", "1")
        self.assertFalse(self.s.delete("a", "y"))

    def test_record_can_be_recreated_after_emptied(self):
        self.s.set("a", "x", "1")
        self.s.delete("a", "x")
        self.s.set("a", "y", "2")
        self.assertEqual(self.s.get("a", "y"), "2")
        self.assertIsNone(self.s.get("a", "x"))


if __name__ == "__main__":
    unittest.main()
