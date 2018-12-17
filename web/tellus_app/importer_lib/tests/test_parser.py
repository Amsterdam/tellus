from unittest import TestCase
from importer_lib.parser import parse_speed_interval, parse_length_interval


class TestParser(TestCase):
    def test_speed_max_only(self):
        self.assertEqual(parse_speed_interval("< 30 km/u"), [None, 30])
        self.assertEqual(parse_speed_interval("< 50 km/u"), [None, 50])

    def test_speed_min_max(self):
        self.assertEqual(parse_speed_interval("31 - 40 km/u"), [31, 40])
        self.assertEqual(parse_speed_interval("91 - 100 km/u"), [91, 100])

    def test_speed_min_only(self):
        self.assertEqual(parse_speed_interval("> 0 km/u"), [0, None])
        self.assertEqual(parse_speed_interval("> 100 km/u"), [100, None])
        self.assertEqual(parse_speed_interval("> 120 km/u"), [120, None])

    def test_length_max_only(self):
        self.assertEqual(parse_length_interval("< 5.0 m"), [None, 500])
        self.assertEqual(parse_length_interval("< 5 m"), [None, 500])

    def test_length_min_max(self):
        self.assertEqual(parse_length_interval("0 - 5,1 m"), [0, 510])
        self.assertEqual(parse_length_interval("5,1 - 5,6 m"), [510, 560])
        self.assertEqual(parse_length_interval("5 - 5 m"), [500, 500])

    def test_length_min_only(self):
        self.assertEqual(parse_length_interval("> 12,2 m"), [1220, None])
        self.assertEqual(parse_length_interval("> 12 m"), [1200, None])
