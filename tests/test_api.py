import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inventory import service, api
from inventory.models import Item


class TestApi(unittest.TestCase):
    def setUp(self):
        service.seed([
            Item(item_id="widget", name="Widget", price=10.0, quantity=3),
        ])

    def test_get_item_found(self):
        status, body = api.handle_get_item("widget")
        self.assertEqual(status, 200)
        self.assertEqual(body["name"], "Widget")

    def test_get_item_not_found(self):
        # Already-satisfied requirement: unknown items must 404.
        status, body = api.handle_get_item("does-not-exist")
        self.assertEqual(status, 404)
        self.assertEqual(body["error"], "not_found")


if __name__ == "__main__":
    unittest.main()
