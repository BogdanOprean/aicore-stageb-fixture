"""Minimal in-process HTTP-style router (stdlib only, no framework dep)."""

from . import service


def handle_get_item(item_id: str) -> tuple[int, dict]:
    try:
        item = service.get_item(item_id)
    except KeyError:
        return 404, {"error": "not_found"}
    return 200, {
        "item_id": item.item_id,
        "name": item.name,
        "price": item.price,
        "quantity": item.quantity,
    }
