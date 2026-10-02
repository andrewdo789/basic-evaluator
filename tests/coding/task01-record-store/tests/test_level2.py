import unittest
from solution import RecordStore


class TestLevel2(unittest.TestCase):
    def setUp(self):
        self.s = RecordStore()

    def test_scan_missing(self):
        self.assertEqual(self.s.scan("a"), [])
        self.assertEqual(self.s.scan_by_prefix("a", "x"), [])

    def test_scan_sorted(self):
        self.s.set("A", "b", "2")
        self.s.set("A", "a", "1")
        self.s.set("A", "c", "3")
        self.assertEqual(self.s.scan("A"), ["a(1)", "b(2)", "c(3)"])

    def test_scan_after_update_and_delete(self):
        self.s.set("A", "b", "2")
        self.s.set("A", "a", "1")
        self.s.set("A", "a", "9")
        self.s.delete("A", "b")
        self.assertEqual(self.s.scan("A"), ["a(9)"])

    def test_scan_string_order(self):
        self.s.set("A", "b10", "x")
        self.s.set("A", "b2", "y")
        self.s.set("A", "B", "z")
        self.assertEqual(self.s.scan("A"), ["B(z)", "b10(x)", "b2(y)"])

    def test_prefix(self):
        for f, v in [("age", "30"), ("address", "x"), ("name", "n"), ("a", "1")]:
            self.s.set("P", f, v)
        self.assertEqual(self.s.scan_by_prefix("P", "a"), ["a(1)", "address(x)", "age(30)"])
        self.assertEqual(self.s.scan_by_prefix("P", "ad"), ["address(x)"])
        self.assertEqual(self.s.scan_by_prefix("P", "z"), [])

    def test_prefix_empty_string_matches_all(self):
        self.s.set("P", "b", "2")
        self.s.set("P", "a", "1")
        self.assertEqual(self.s.scan_by_prefix("P", ""), ["a(1)", "b(2)"])

    def test_scan_does_not_mix_records(self):
        self.s.set("A", "x", "1")
        self.s.set("B", "y", "2")
        self.assertEqual(self.s.scan("A"), ["x(1)"])
        self.assertEqual(self.s.scan("B"), ["y(2)"])


if __name__ == "__main__":
    unittest.main()
