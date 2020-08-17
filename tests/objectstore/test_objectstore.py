from unittest import TestCase

from objectstore import objectstore


class TestObjectStore(TestCase):
    def test_os_connect(self):
        assert objectstore.os_connect["user"] == "tellus"
        assert objectstore.os_connect["tenant_name"] == "BGE000081_Tellus"

    def test_split_prefix(self):
        assert "first_part" == objectstore.split_prefix("first_part_second")
