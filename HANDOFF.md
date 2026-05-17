# Flying Star Calculator — Cool Handoff

## Status

Phase 1 implemented locally with six validated lookup cases.

## Project Path

`~/sandbox/flying-star-calculator/`

## Files Created

```text
flying-star-calculator/
├── HANDOFF.md
├── SPEC.md
├── src/
│   ├── __init__.py
│   ├── engine/
│   │   ├── __init__.py
│   │   ├── base_chart.py
│   │   ├── lookup.py
│   │   └── validator.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── chart.py
│   │   └── sector.py
│   └── cli/
│       ├── __init__.py
│       └── main.py
└── tests/
    ├── fixtures/
    │   └── master_validation.json
    └── test_lookup_validation.py
```

## CLI Usage

```bash
python -m src.cli.main --period 9 --facing SE
python -m src.cli.main --period 9 --facing SE --format json
python -m src.cli.main --period 9 --facing SE --debug
```

## Validation

```bash
python3 tests/test_lookup_validation.py
```

Expected: `Results: 6/6 passed`.

## Notes

- Lookup-first only.
- No formula derivation.
- No external scraping or WOFS code copying.
- Only the six validated cases are supported.
