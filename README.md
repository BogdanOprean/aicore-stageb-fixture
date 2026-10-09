# Inventory Service

A tiny inventory-tracking service used as a disposable fixture for AI-CORE
Stage B autonomy acceptance testing. Do not use this repository for anything
else — it is intentionally small, intentionally buggy in places, and will be
mutated by automated coding-agent tasks.

## Layout

- `src/inventory/models.py` — the `Item` data model shared by the service and
  API layers.
- `src/inventory/service.py` — business logic (stock, discounting, restocking).
- `src/inventory/api.py` — a minimal in-process HTTP-style request router
  (no external framework dependency) exposing the service over simple
  dict-based "requests" so the fixture runs with only the stdlib.
- `config.json` — service configuration (currency, low-stock threshold).
- `tests/` — a deterministic unit test suite (`unittest`, stdlib only).

## Running tests

```sh
python -m unittest discover -s tests -v
```

## Known issues (tracked, intentionally unfixed at baseline)

- `apply_discount` in `service.py` computes the discount incorrectly
  (see `tests/test_service.py::test_apply_discount_percentage`, which fails
  at baseline). Tracked as fixture defect FX-1.
