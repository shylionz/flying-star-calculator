#!/usr/bin/env python3
"""Invariant tests for compass ring-shift overlay mode."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.engine.base_chart import generate_natal_chart
from src.orientation.transform import (
    apply_ring_shift,
    assert_preserves_palace_star_assignments,
    decrement_ring_shift,
    increment_ring_shift,
    palace_star_signature_from_grid,
)

VALIDATED_CASES = ((9, "SE"), (8, "N1"), (8, "SW2"), (9, "E1"), (7, "W2"), (6, "NE3"))
SHIFT_RANGE = range(-8, 9)


def _flat(grid):
    return [cell for row in grid for cell in row]


def _palace_layout(grid):
    return tuple(tuple(cell["canonical_palace"] for cell in row) for row in grid)


def _cell_at_display_palace(grid, display_palace):
    for cell in _flat(grid):
        if cell.get("display_palace") == display_palace:
            return cell
    raise AssertionError(f"display palace not found: {display_palace}")


def run_all_tests():
    results = {"passed": 0, "failed": 0}
    all_errors = []
    print("Running ring-shift invariant tests...")
    print("-" * 50)

    for period, facing in VALIDATED_CASES:
        errors = []
        chart = generate_natal_chart(period, facing)
        canonical_ascii_before = chart.to_ascii()
        zero_grid = apply_ring_shift(chart, 0)
        zero_layout = _palace_layout(zero_grid)

        for steps in SHIFT_RANGE:
            grid = apply_ring_shift(chart, steps)
            try:
                assert_preserves_palace_star_assignments(chart, grid)
            except AssertionError as exc:
                errors.append(f"P{period}/{facing} shift {steps}: {exc}")

            center = _cell_at_display_palace(grid, "C")
            if center["canonical_palace"] != "C":
                errors.append(f"P{period}/{facing} shift {steps}: C moved to {center['canonical_palace']}")

            if len(grid) != 3 or any(len(row) != 3 for row in grid) or len(_flat(grid)) != 9:
                errors.append(f"P{period}/{facing} shift {steps}: not a full 3x3 grid")

            if len(palace_star_signature_from_grid(grid)) != 9:
                errors.append(f"P{period}/{facing} shift {steps}: duplicate/lost palace-star signature")

        if _palace_layout(apply_ring_shift(chart, 8)) != zero_layout:
            errors.append(f"P{period}/{facing}: shift +8 did not return original layout")

        current_steps = 0
        current_steps = increment_ring_shift(current_steps)
        current_steps = decrement_ring_shift(current_steps)
        if current_steps != 0 or _palace_layout(apply_ring_shift(chart, current_steps)) != zero_layout:
            errors.append(f"P{period}/{facing}: +1 then -1 did not return original")

        cumulative = 0
        cumulative = increment_ring_shift(cumulative)
        cumulative = increment_ring_shift(cumulative)
        cumulative = increment_ring_shift(cumulative)
        if cumulative != 3 or _palace_layout(apply_ring_shift(chart, cumulative)) != _palace_layout(apply_ring_shift(chart, 3)):
            errors.append(f"P{period}/{facing}: multiple clicks were not cumulative")

        shifted_plus_one = apply_ring_shift(chart, 1)
        ne_cell = _cell_at_display_palace(shifted_plus_one, "NE")
        if ne_cell["canonical_palace"] != "N":
            errors.append(f"P{period}/{facing}: canonical N did not move to NE after shift +1")

        if chart.to_ascii() != canonical_ascii_before:
            errors.append(f"P{period}/{facing}: ring shift altered lookup engine chart output")

        if errors:
            results["failed"] += 1
            all_errors.extend(errors)
            print(f"FAIL P{period} {facing}")
            for error in errors:
                print(f" - {error}")
        else:
            results["passed"] += 1
            print(f"PASS P{period} {facing}")

    print("-" * 50)
    total = results["passed"] + results["failed"]
    print(f"Results: {results['passed']}/{total} passed")
    return results, all_errors


if __name__ == "__main__":
    results, errors = run_all_tests()
    sys.exit(0 if not errors else 1)
