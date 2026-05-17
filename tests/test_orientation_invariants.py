#!/usr/bin/env python3
"""Invariant tests for the Phase 2 orientation/overlay layer."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.engine.base_chart import generate_natal_chart
from src.orientation.transform import (
    assert_preserves_palace_star_assignments,
    oriented_grid,
    palace_star_signature_from_chart,
    palace_star_signature_from_grid,
)

ORIENTATIONS = ("top", "right", "bottom", "left")
VALIDATED_CASES = ((9, "SE2"), (8, "N1"), (8, "SW2"), (9, "E1"), (7, "W2"), (6, "NE3"))


def _flat(grid):
    return [cell for row in grid for cell in row]


def test_orientation_preserves_assignments_for_case(period, facing):
    chart = generate_natal_chart(period, facing)
    canonical_signature = palace_star_signature_from_chart(chart)
    errors = []

    for orientation in ORIENTATIONS:
        grid = oriented_grid(chart, orientation)
        try:
            assert_preserves_palace_star_assignments(chart, grid)
        except AssertionError as exc:
            errors.append(f"{orientation}: {exc}")

        if palace_star_signature_from_grid(grid) != canonical_signature:
            errors.append(f"{orientation}: signature mismatch")
        if len(grid) != 3 or any(len(row) != 3 for row in grid):
            errors.append(f"{orientation}: not a 3x3 grid")
        if len(_flat(grid)) != 9:
            errors.append(f"{orientation}: does not contain 9 cells")

    return errors


def test_known_bottom_rotation_mapping():
    chart = generate_natal_chart(9, "SE2")
    grid = oriented_grid(chart, "bottom")
    expected = (("NW", "N", "NE"), ("W", "C", "E"), ("SW", "S", "SE"))
    actual = tuple(tuple(cell["canonical_palace"] for cell in row) for row in grid)
    return [] if actual == expected else [f"bottom mapping {actual} != {expected}"]


def run_all_tests():
    results = {"passed": 0, "failed": 0}
    print("Running orientation invariant tests...")
    print("-" * 50)

    for period, facing in VALIDATED_CASES:
        errors = test_orientation_preserves_assignments_for_case(period, facing)
        if errors:
            results["failed"] += 1
            print(f"FAIL P{period} {facing}")
            for error in errors:
                print(f" - {error}")
        else:
            results["passed"] += 1
            print(f"PASS P{period} {facing}")

    mapping_errors = test_known_bottom_rotation_mapping()
    if mapping_errors:
        results["failed"] += 1
        print("FAIL bottom rotation mapping")
        for error in mapping_errors:
            print(f" - {error}")
    else:
        results["passed"] += 1
        print("PASS bottom rotation mapping")

    print("-" * 50)
    total = results["passed"] + results["failed"]
    print(f"Results: {results['passed']}/{total} passed")
    return results


if __name__ == "__main__":
    results = run_all_tests()
    sys.exit(0 if results["failed"] == 0 else 1)
