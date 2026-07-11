"""Annual Flying Star overlay engine.

Annual stars are independent guest stars. They are composed with natal palace
data later, but this module never imports or mutates natal chart objects.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

PALACES = ("SE", "S", "SW", "E", "C", "W", "NE", "N", "NW")
LO_SHU_FLIGHT_PATH = ("C", "NW", "W", "NE", "S", "N", "SW", "E", "SE")

# Stage 2 validation references:
# - 2025: Fengshuiweb confirms center #2 and sector placements including
#   N7, NE5, W4, NW3, E9, SW8. Lighthouse Feng Shui search-index text confirms
#   SE1, SW8, S6, E9. Standard forward Lo Shu flight fills the complete map.
# - 2026: FengShuiBalanz/Potala confirm the Li Chun Feb 4 shift and 2026
#   center #1; standard forward Lo Shu flight yields the full sector map.
PUBLISHED_ANNUAL_REFERENCE_MAPS = {
    2025: {"C": 2, "NW": 3, "W": 4, "NE": 5, "S": 6, "N": 7, "SW": 8, "E": 9, "SE": 1},
    2026: {"C": 1, "NW": 2, "W": 3, "NE": 4, "S": 5, "N": 6, "SW": 7, "E": 8, "SE": 9},
}


@dataclass(frozen=True)
class AnnualOverlay:
    flying_star_year: int
    center_star: int
    stars: dict[str, int]
    source: str = "annual_decrement_lo_shu_forward_flight"


def _star_after_steps(center_star: int, steps: int) -> int:
    return ((center_star - 1 + steps) % 9) + 1


def fly_stars_from_center(center_star: int) -> dict[str, int]:
    """Return canonical palace -> star using standard forward Lo Shu flight."""
    if center_star not in range(1, 10):
        raise ValueError("center_star must be 1..9")
    return {
        palace: _star_after_steps(center_star, offset)
        for offset, palace in enumerate(LO_SHU_FLIGHT_PATH)
    }


def annual_center_star(flying_star_year: int) -> int:
    """Return the annual center star for a Flying Star year.

    The accepted modern annual sequence has 2024 center 3, 2025 center 2,
    2026 center 1, then wraps to 9.
    """
    year_delta = int(flying_star_year) - 2026
    return ((1 - 1 - year_delta) % 9) + 1


def flying_star_year_for_date(value: date) -> int:
    """Resolve a Gregorian date to Flying Star year using Li Chun on Feb 4.

    Stage 2 only needs date-level rollover behavior. Stage 3 will replace this
    with exact solar-term timestamps from the solar term resolver.
    """
    if not isinstance(value, date):
        raise TypeError("value must be a datetime.date")
    if (value.month, value.day) < (2, 4):
        return value.year - 1
    return value.year


def annual_overlay_for_year(flying_star_year: int) -> AnnualOverlay:
    center = annual_center_star(flying_star_year)
    return AnnualOverlay(
        flying_star_year=int(flying_star_year),
        center_star=center,
        stars=fly_stars_from_center(center),
    )


def annual_overlay_for_date(value: date) -> AnnualOverlay:
    return annual_overlay_for_year(flying_star_year_for_date(value))


def validate_annual_map(stars: dict[str, int]) -> None:
    if set(stars) != set(PALACES):
        raise AssertionError("annual overlay must contain all nine canonical palaces")
    if sorted(stars.values()) != list(range(1, 10)):
        raise AssertionError("annual overlay must contain stars 1..9 exactly once")
