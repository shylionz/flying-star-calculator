"""Simplified Gregorian-month Flying Star overlay engine.

This version treats January through December as whole calendar months.
It does not calculate exact Jie Qi transition dates.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.temporal.annual import PALACES, fly_stars_from_center


MONTH_NAMES = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}


MONTHLY_CENTER_STARS = {
    2025: {
        1: 3,
        2: 2,
        3: 1,
        4: 9,
        5: 8,
        6: 7,
        7: 6,
        8: 5,
        9: 4,
        10: 3,
        11: 2,
        12: 1,
    },
    2026: {
        1: 9,
        2: 8,
        3: 7,
        4: 6,
        5: 5,
        6: 4,
        7: 3,
        8: 2,
        9: 1,
        10: 9,
        11: 8,
        12: 7,
    },
}


@dataclass(frozen=True)
class MonthlyOverlay:
    year: int
    month: int
    month_name: str
    center_star: int
    stars: dict[str, int]


def monthly_center_star(year: int, month: int) -> int:
    year = int(year)
    month = int(month)

    if year not in MONTHLY_CENTER_STARS:
        raise ValueError(
            f"Unsupported year: {year}. "
            f"Supported years: {sorted(MONTHLY_CENTER_STARS)}"
        )

    if month not in range(1, 13):
        raise ValueError("month must be 1..12")

    return MONTHLY_CENTER_STARS[year][month]


def monthly_overlay(year: int, month: int) -> MonthlyOverlay:
    center = monthly_center_star(year, month)

    return MonthlyOverlay(
        year=year,
        month=month,
        month_name=MONTH_NAMES[month],
        center_star=center,
        stars=fly_stars_from_center(center),
    )


def validate_monthly_map(stars: dict[str, int]) -> None:
    if set(stars) != set(PALACES):
        raise AssertionError(
            "monthly overlay must contain all nine canonical palaces"
        )

    if sorted(stars.values()) != list(range(1, 10)):
        raise AssertionError(
            "monthly overlay must contain stars 1..9 exactly once"
        )
