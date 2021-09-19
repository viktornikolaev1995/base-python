import unittest

class TestPython(unittest.TestCase):
    def test_float_to_int_correction(self):
        self.assertEqual(1, int("1.6"))
    def test_get_empty_dict(self):
        self.assertIsNone({"key": 4}.get("key"))
    def test_trueness(self):
        self.assertTrue(bool(0))
