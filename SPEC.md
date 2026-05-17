# Flying Star Calculator — Phase 1 Spec

## Scope

Build a local lookup-first Flying Star natal chart calculator for exactly six validated cases.

## Rules

- Use lookup-first implementation.
- Do not derive formulas.
- Do not scrape or copy WOFS code.
- Support only the six validated fixture cases until more cases are explicitly added.
- `src/__init__.py` is the package marker; do not use `src/init.py`.

## Supported Cases

- Period 9 / SE
- Period 8 / N1
- Period 8 / SW2
- Period 9 / E1
- Period 7 / W2
- Period 6 / NE3

## CLI

```bash
python -m src.cli.main --period 9 --facing SE
python -m src.cli.main --period 9 --facing SE --format json
python -m src.cli.main --period 9 --facing SE --debug
```

## Validation Gate

```bash
python3 tests/test_lookup_validation.py
```

Expected: 6/6 passed.
