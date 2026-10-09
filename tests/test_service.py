import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inventory import service
from inventory.models import Item


class TestService(unittest.TestCase):
    def setUp(self):
        service.seed([
            Item(item_id="widget", name="Widget", price=10.0, quantity=3),
            Item(item_id="gadget", name="Gadget", price=20.0, quantity=50),
        ])

    def test_get_item(self):
        item = service.get_item("widget")
        self.assertEqual(item.name, "Widget")

    def test_apply_discount_percentage(self):
        # FX-1: fixture defect. 10.0 with a 20% discount must be 8.0.
        self.assertEqual(service.apply_discount(10.0, 20), 8.0)

    def test_is_low_stock_true(self):
        self.assertTrue(service.is_low_stock("widget", threshold=5))

    def test_is_low_stock_false(self):
        self.assertFalse(service.is_low_stock("gadget", threshold=5))


if __name__ == "__main__":
    unittest.main()
