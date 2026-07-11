#!/usr/bin/env python3
"""Validation tests for annual Flying Star overlays."""
from datetime import date
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.engine.base_chart import generate_natal_chart
from src.temporal.annual import (
    PUBLISHED_ANNUAL_REFERENCE_MAPS,
    annual_center_star,
    annual_overlay_for_date,
    annual_overlay_for_year,
    fly_stars_from_center,
    flying_star_year_for_date,
    validate_annual_map,
)


def _assert(condition, message, errors):
    if not condition:
        errors.append(message)


def test_full_published_maps():
    errors = []
    for year, expected in PUBLISHED_ANNUAL_REFERENCE_MAPS.items():
        overlay = annual_overlay_for_year(year)
        try:
            validate_annual_map(overlay.stars)
        except AssertionError as exc:
            errors.append(f"{year}: {exc}")
        _assert(overlay.stars == expected, f"{year}: {overlay.stars} != {expected}", errors)
    return errors


def test_center_targets():
    errors = []
    _assert(annual_center_star(2025) == 2, "2025 center must be 2", errors)
    _assert(annual_center_star(2026) == 1, "2026 center must be 1", errors)
    _assert(annual_center_star(2027) == 9, "2027 center must wrap to 9", errors)
    return errors


def test_uniqueness_for_cycle():
    errors = []
    for center in range(1, 10):
        stars = fly_stars_from_center(center)
        try:
            validate_annual_map(stars)
        except AssertionError as exc:
            errors.append(f"center {center}: {exc}")
    return errors


def test_li_chun_year_rollover():
    errors = []
    cases = (
        (date(2026, 1, 1), 2025, 2),
        (date(2026, 2, 3), 2025, 2),
        (date(2026, 2, 4), 2026, 1),
        (date(2027, 2, 3), 2026, 1),
        (date(2027, 2, 4), 2027, 9),
    )
    for value, expected_year, expected_center in cases:
        overlay = annual_overlay_for_date(value)
        _assert(flying_star_year_for_date(value) == expected_year, f"{value}: wrong FS year", errors)
        _assert(overlay.flying_star_year == expected_year, f"{value}: overlay year mismatch", errors)
        _assert(overlay.center_star == expected_center, f"{value}: wrong center", errors)
    return errors


def test_annual_independent_of_natal_chart():
    errors = []
    chart = generate_natal_chart(9, "SE2")
    before = chart.to_ascii()
    overlay = annual_overlay_for_year(2026)
    _assert(overlay.stars["C"] == 1, "annual overlay sanity failed", errors)
    _assert(chart.to_ascii() == before, "annual overlay changed natal chart", errors)
    return errors


def run_all_tests():
    tests = (
        ("full published annual maps", test_full_published_maps),
        ("annual center targets", test_center_targets),
        ("annual uniqueness cycle", test_uniqueness_for_cycle),
        ("Li Chun rollover", test_li_chun_year_rollover),
        ("natal independence", test_annual_independent_of_natal_chart),
    )
    results = {"passed": 0, "failed": 0}
    print("Running annual Flying Star tests...")
    print("-" * 50)
    for name, fn in tests:
        errors = fn()
        if errors:
            results["failed"] += 1
            print(f"FAIL {name}")
            for error in errors:
                print(f" - {error}")
        else:
            results["passed"] += 1
            print(f"PASS {name}")
    print("-" * 50)
    total = results["passed"] + results["failed"]
    print(f"Results: {results['passed']}/{total} passed")
    return results


if __name__ == "__main__":
    results = run_all_tests()
    sys.exit(0 if results["failed"] == 0 else 1)

