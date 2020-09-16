from unittest import TestCase

from importer_lib.parser import parse_length_interval, parse_speed_interval


class TestParser(TestCase):
    def test_speed_max_only(self):
        self.assertEqual([None, 30], parse_speed_interval("< 30 km/u"))
        self.assertEqual([None, 50], parse_speed_interval("< 50 km/u"))

    def test_speed_min_max(self):
        self.assertEqual([31, 40], parse_speed_interval("31 - 40 km/u"))
        self.assertEqual([91, 100], parse_speed_interval("91 - 100 km/u"))

    def test_speed_min_only(self):
        self.assertEqual([0, None], parse_speed_interval("> 0 km/u"))
        self.assertEqual([100, None], parse_speed_interval("> 100 km/u"))
        self.assertEqual([120, None], parse_speed_interval("> 120 km/u"))

    def test_length_max_only(self):
        self.assertEqual([None, 500], parse_length_interval("< 5.0 m"))
        self.assertEqual([None, 500], parse_length_interval("< 5 m"))

    def test_length_min_max(self):
        self.assertEqual([0, 510], parse_length_interval("0 - 5,1 m"))
        self.assertEqual([510, 560], parse_length_interval("5,1 - 5,6 m"))
        self.assertEqual([500, 500], parse_length_interval("5 - 5 m"))

    def test_length_min_only(self):
        self.assertEqual([1220, None], parse_length_interval("> 12,2 m"))
        self.assertEqual([1200, None], parse_length_interval("> 12 m"))
