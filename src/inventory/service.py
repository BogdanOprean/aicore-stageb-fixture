"""Business logic for the inventory fixture service."""

from .models import Item

_CATALOG: dict[str, Item] = {}


def seed(items: list[Item]) -> None:
    _CATALOG.clear()
    for item in items:
        _CATALOG[item.item_id] = item


def get_item(item_id: str) -> Item:
    return _CATALOG[item_id]


def apply_discount(price: float, pct: float) -> float:
    """Return `price` reduced by `pct` percent (pct is 0-100).

    FX-1 (deliberate defect): this currently adds the percentage instead
    of subtracting a fraction of the price.
    """
    return price + pct


def restock(item_id: str, qty: int) -> Item:
    """Increase an item's quantity by `qty` and return the updated item.

    Not yet implemented - Stage B L3-2 fixture feature target.
    """
    raise NotImplementedError("restock is not implemented yet")


def is_low_stock(item_id: str, threshold: int) -> bool:
    return _CATALOG[item_id].quantity < threshold
