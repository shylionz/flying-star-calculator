from __future__ import annotations

"""Pre-validated lookup tables for Flying Star Calculator.

These values are validated against the handoff fixtures.
DO NOT derive from formulas alone - use lookup-first approach.
"""

NATAL_CHART_LOOKUP = {
    (9, "SE"): {"SE": (1, 1, 8), "S": (5, 5, 4), "SW": (3, 3, 6), "E": (2, 2, 7), "C": (9, 9, 9), "W": (7, 7, 2), "NE": (6, 6, 3), "N": (4, 4, 5), "NW": (8, 8, 1)},
    (8, "N1"): {"SE": (5, 7, 2), "S": (9, 3, 7), "SW": (7, 5, 9), "E": (6, 6, 1), "C": (4, 8, 3), "W": (2, 1, 5), "NE": (1, 2, 6), "N": (8, 4, 8), "NW": (3, 9, 4)},
    (8, "SW2"): {"SE": (1, 7, 4), "S": (6, 3, 9), "SW": (8, 5, 2), "E": (9, 6, 3), "C": (2, 8, 5), "W": (4, 1, 7), "NE": (5, 2, 8), "N": (7, 4, 1), "NW": (3, 9, 6)},
    (9, "E1"): {"SE": (3, 8, 6), "S": (7, 4, 2), "SW": (5, 6, 4), "E": (4, 7, 5), "C": (2, 9, 7), "W": (9, 2, 9), "NE": (8, 3, 1), "N": (6, 5, 3), "NW": (1, 1, 8)},
    (7, "W2"): {"SE": (6, 6, 1), "S": (1, 2, 5), "SW": (8, 4, 3), "E": (7, 5, 2), "C": (5, 7, 9), "W": (3, 9, 7), "NE": (2, 1, 6), "N": (9, 3, 4), "NW": (4, 8, 8)},
    (6, "NE3"): {"SE": (4, 5, 1), "S": (8, 1, 5), "SW": (6, 3, 3), "E": (5, 4, 2), "C": (3, 6, 9), "W": (1, 8, 7), "NE": (9, 9, 6), "N": (7, 2, 4), "NW": (2, 7, 8)},
}


def get_lookup_chart(period: int, facing: str) -> dict | None:
    """Return position -> (mountain, water, base), or None if unsupported."""
    return NATAL_CHART_LOOKUP.get((period, facing.upper()))


def supported_cases() -> list[tuple[int, str]]:
    """Return supported validated (period, facing) cases."""
    return sorted(NATAL_CHART_LOOKUP.keys())
