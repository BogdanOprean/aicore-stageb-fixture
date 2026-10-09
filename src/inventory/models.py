"""Shared data model consumed by both service.py and api.py."""

from dataclasses import dataclass


@dataclass
class Item:
    item_id: str
    name: str
    price: float
    quantity: int
