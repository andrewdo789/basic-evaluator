import unittest
from solution import RecordStore


class TestLevel3(unittest.TestCase):
    def setUp(self):
        self.s = RecordStore()

    def test_set_at_permanent(self):
        self.s.set_at("a", "x", "1", 1)
        self.assertEqual(self.s.get_at("a", "x", 1000), "1")

    def test_ttl_window_is_half_open(self):
        self.s.set_at_with_ttl("a", "x", "1", 10, 5)
        self.assertEqual(self.s.get_at("a", "x", 11), "1")
        self.assertEqual(self.s.get_at("a", "x", 14), "1")
        self.assertIsNone(self.s.get_at("a", "x", 15))

    def test_reset_replaces_expiry(self):
        self.s.set_at_with_ttl("a", "x", "1", 10, 5)
        self.s.set_at_with_ttl("a", "x", "2", 12, 100)
        self.assertEqual(self.s.get_at("a", "x", 50), "2")
        self.s.set_at("a", "x", "3", 60)
        self.assertEqual(self.s.get_at("a", "x", 10_000), "3")

    def test_plain_set_after_ttl_makes_permanent(self):
        self.s.set_at_with_ttl("a", "x", "1", 1, 3)
        self.s.set_at("a", "x", "2", 2)
        self.assertEqual(self.s.get_at("a", "x", 500), "2")

    def test_delete_at(self):
        self.s.set_at_with_ttl("a", "x", "1", 10, 5)
        self.s.set_at("a", "y", "2", 11)
        self.assertTrue(self.s.delete_at("a", "y", 12))
        self.assertFalse(self.s.delete_at("a", "x", 20))
        self.assertFalse(self.s.delete_at("a", "y", 21))

    def test_scan_at_hides_expired(self):
        self.s.set_at_with_ttl("A", "b", "2", 1, 10)
        self.s.set_at("A", "a", "1", 2)
        self.s.set_at_with_ttl("A", "c", "3", 3, 100)
        self.assertEqual(self.s.scan_at("A", 5), ["a(1)", "b(2)", "c(3)"])
        self.assertEqual(self.s.scan_at("A", 11), ["a(1)", "c(3)"])
        self.assertEqual(self.s.scan_by_prefix_at("A", "b", 12), [])
        self.assertEqual(self.s.scan_by_prefix_at("A", "c", 13), ["c(3)"])

    def test_expired_record_is_empty(self):
        self.s.set_at_with_ttl("A", "x", "1", 1, 2)
        self.assertEqual(self.s.scan_at("A", 3), [])
        self.assertIsNone(self.s.get_at("A", "x", 4))

    def test_set_after_expiry(self):
        self.s.set_at_with_ttl("A", "x", "1", 1, 2)
        self.s.set_at("A", "x", "5", 10)
        self.assertEqual(self.s.get_at("A", "x", 11), "5")


if __name__ == "__main__":
    unittest.main()
