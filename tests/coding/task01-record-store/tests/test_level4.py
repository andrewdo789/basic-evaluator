import unittest
from solution import RecordStore


class TestLevel4(unittest.TestCase):
    def setUp(self):
        self.s = RecordStore()

    def test_backup_counts_live_records(self):
        self.s.set_at("A", "x", "1", 1)
        self.s.set_at_with_ttl("B", "x", "1", 2, 3)
        self.s.set_at("C", "x", "1", 3)
        self.s.delete_at("C", "x", 4)
        self.assertEqual(self.s.backup(5), 1)
        self.assertEqual(self.s.backup(6), 1)

    def test_backup_counts_ttl_record_while_live(self):
        self.s.set_at("A", "x", "1", 1)
        self.s.set_at_with_ttl("B", "x", "1", 2, 10)
        self.assertEqual(self.s.backup(3), 2)

    def test_backup_empty(self):
        self.assertEqual(self.s.backup(1), 0)

    def test_restore_rolls_back_changes(self):
        self.s.set_at("A", "x", "1", 1)
        self.s.backup(2)
        self.s.set_at("A", "x", "2", 3)
        self.s.set_at("B", "y", "3", 4)
        self.s.restore(5, 2)
        self.assertEqual(self.s.get_at("A", "x", 6), "1")
        self.assertIsNone(self.s.get_at("B", "y", 7))

    def test_restore_picks_latest_backup_at_or_before(self):
        self.s.set_at("A", "x", "1", 1)
        self.s.backup(2)
        self.s.set_at("A", "x", "2", 3)
        self.s.backup(4)
        self.s.set_at("A", "x", "3", 5)
        self.s.backup(6)
        self.s.restore(7, 5)
        self.assertEqual(self.s.get_at("A", "x", 8), "2")
        self.s.restore(9, 4)
        self.assertEqual(self.s.get_at("A", "x", 10), "2")
        self.s.restore(11, 3)
        self.assertEqual(self.s.get_at("A", "x", 12), "1")

    def test_restore_recomputes_ttl(self):
        self.s.set_at_with_ttl("A", "x", "1", 10, 20)
        self.s.backup(15)
        self.s.restore(100, 15)
        self.assertEqual(self.s.get_at("A", "x", 114), "1")
        self.assertIsNone(self.s.get_at("A", "x", 115))

    def test_expired_at_backup_stays_gone(self):
        self.s.set_at_with_ttl("A", "x", "1", 1, 2)
        self.s.set_at("A", "y", "2", 2)
        self.s.backup(5)
        self.s.restore(6, 5)
        self.assertEqual(self.s.scan_at("A", 7), ["y(2)"])

    def test_backup_is_a_snapshot_not_a_reference(self):
        self.s.set_at("A", "x", "1", 1)
        self.s.backup(2)
        self.s.set_at("A", "x", "2", 3)
        self.s.delete_at("A", "x", 4)
        self.s.restore(5, 2)
        self.assertEqual(self.s.get_at("A", "x", 6), "1")
        self.s.set_at("A", "x", "9", 7)
        self.s.restore(8, 2)
        self.assertEqual(self.s.get_at("A", "x", 9), "1")

    def test_permanent_fields_survive_restore(self):
        self.s.set_at("A", "x", "1", 1)
        self.s.backup(2)
        self.s.restore(1_000, 2)
        self.assertEqual(self.s.get_at("A", "x", 1_000_000), "1")


if __name__ == "__main__":
    unittest.main()
