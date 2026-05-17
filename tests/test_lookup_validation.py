#!/usr/bin/env python3
"""
Automated validation tests for Flying Star Calculator.
Uses fixtures from tests/fixtures/master_validation.json.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.engine.base_chart import generate_natal_chart


def load_validation_fixtures():
    fixture_path = os.path.join(os.path.dirname(__file__), "fixtures", "master_validation.json")
    with open(fixture_path, encoding="utf-8") as f:
        return json.load(f)


def test_single_case(tc):
    errors = []
    chart = generate_natal_chart(tc["period"], tc["facing"])

    for sector in chart.sectors:
        pos = sector.position
        expected = tc["grid"][pos]
        if sector.mountain_star != expected["mountain"]:
            errors.append(f"{pos}: mountain {sector.mountain_star} != {expected['mountain']}")
        if sector.water_star != expected["water"]:
            errors.append(f"{pos}: water {sector.water_star} != {expected['water']}")
        if sector.base_star != expected["base"]:
            errors.append(f"{pos}: base {sector.base_star} != {expected['base']}")

    return errors


def run_all_tests():
    data = load_validation_fixtures()
    results = {"passed": 0, "failed": 0, "cases": []}

    print(f"Running {data['total_cases']} validation cases...")
    print("-" * 50)

    for tc in data["test_cases"]:
        errors = test_single_case(tc)
        case_result = {"id": tc["id"], "period": tc["period"], "facing": tc["facing"], "errors": errors}

        if errors:
            results["failed"] += 1
            print(f"FAIL {tc['id']}: P{tc['period']} {tc['facing']} - FAILED")
            for error in errors:
                print(f" - {error}")
        else:
            results["passed"] += 1
            print(f"PASS {tc['id']}: P{tc['period']} {tc['facing']} - PASSED")

        results["cases"].append(case_result)

    print("-" * 50)
    print(f"Results: {results['passed']}/{results['passed'] + results['failed']} passed")
    return results


if __name__ == "__main__":
    results = run_all_tests()
    sys.exit(0 if results["failed"] == 0 else 1)
