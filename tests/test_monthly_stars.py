#!/usr/bin/env python3

import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT))

from src.temporal.monthly import (
    MONTHLY_CENTER_STARS,
    monthly_center_star,
    monthly_overlay,
    validate_monthly_map,
)


def run_tests() -> None:
    tests_run = 0

    assert len(MONTHLY_CENTER_STARS[2025]) == 12
    assert len(MONTHLY_CENTER_STARS[2026]) == 12
    tests_run += 1
    print("PASS monthly lookup contains 12 months per year")

    assert monthly_center_star(2026, 1) == 9
    assert monthly_center_star(2026, 3) == 7
    assert monthly_center_star(2025, 11) == 2
    tests_run += 1
    print("PASS known monthly center examples")

    for year in (2025, 2026):
        for month in range(1, 13):
            overlay = monthly_overlay(year, month)
            validate_monthly_map(overlay.stars)
            assert overlay.stars["C"] == overlay.center_star

    tests_run += 1
    print("PASS all 24 monthly overlays")

    march_2026 = monthly_overlay(2026, 3)

    assert march_2026.center_star == 7
    assert march_2026.stars == {
        "C": 7,
        "NW": 8,
        "W": 9,
        "NE": 1,
        "S": 2,
        "N": 3,
        "SW": 4,
        "E": 5,
        "SE": 6,
    }

    tests_run += 1
    print("PASS March 2026 full palace map")

    try:
        monthly_center_star(2026, 13)
        raise AssertionError("month 13 should fail")
    except ValueError:
        pass

    try:
        monthly_center_star(2027, 1)
        raise AssertionError("unsupported year should fail")
    except ValueError:
        pass

    tests_run += 1
    print("PASS invalid input validation")

    print("-" * 50)
    print(f"Results: {tests_run}/{tests_run} passed")


if __name__ == "__main__":
    run_tests()
