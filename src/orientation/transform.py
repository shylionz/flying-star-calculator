"""Transform canonical natal charts into visual overlay grids.

No star values are recalculated here. The module copies canonical palace-star
assignments into display positions only.
"""
from __future__ import annotations

from typing import Any

from src.models.chart import DISPLAY_ROWS, NatalChart
from src.models.sector import Sector
from src.orientation.rotation import rotate_matrix, rotation_degrees_for_orientation

DISPLAY_POSITIONS = (
    ("top-left", "top-center", "top-right"),
    ("middle-left", "center", "middle-right"),
    ("bottom-left", "bottom-center", "bottom-right"),
)

COMPASS_RING_ORDER = ("NW", "N", "NE", "E", "SE", "S", "SW", "W")
PALACE_TO_DISPLAY_INDEX = {
    position: (row_index, column_index)
    for row_index, row in enumerate(DISPLAY_ROWS)
    for column_index, position in enumerate(row)
}


def _sector_to_cell(sector: Sector) -> dict[str, Any]:
    return {
        "canonical_palace": sector.position,
        "mountain": sector.mountain_star,
        "water": sector.water_star,
        "base": sector.base_star,
    }


def canonical_matrix(chart: NatalChart) -> list[list[dict[str, Any]]]:
    """Return canonical SE/S/SW, E/C/W, NE/N/NW palace matrix."""
    sector_map = chart.sector_map()
    return [[_sector_to_cell(sector_map[position]) for position in row] for row in DISPLAY_ROWS]


def oriented_grid(chart: NatalChart, orientation: str = "top") -> list[list[dict[str, Any]]]:
    """Return a visually rotated 3x3 display grid.

    Matrix rotation is a 90/180/270 visual transform. It is distinct from
    compass ring shifting. Palace identity and star triples are preserved.
    """
    degrees = rotation_degrees_for_orientation(orientation)
    rotated = rotate_matrix(canonical_matrix(chart), orientation)

    output = []
    for r, row in enumerate(rotated):
        output_row = []
        for c, cell in enumerate(row):
            output_row.append(
                {
                    "display_position": DISPLAY_POSITIONS[r][c],
                    "canonical_palace": cell["canonical_palace"],
                    "mountain": cell["mountain"],
                    "water": cell["water"],
                    "base": cell["base"],
                    "orientation_mode": "matrix_rotation",
                    "rotation_applied": degrees,
                    "ring_shift_steps": 0,
                }
            )
        output.append(output_row)
    return output


def _empty_display_grid() -> list[list[dict[str, Any] | None]]:
    return [[None for _ in range(3)] for _ in range(3)]


def _finalize_grid(grid: list[list[dict[str, Any] | None]]) -> list[list[dict[str, Any]]]:
    finalized: list[list[dict[str, Any]]] = []
    for row in grid:
        finalized_row = []
        for cell in row:
            if cell is None:
                raise AssertionError("incomplete display grid")
            finalized_row.append(cell)
        finalized.append(finalized_row)
    return finalized


def normalize_ring_shift(steps: int) -> int:
    """Normalize cumulative ring-shift steps to the 0-7 display cycle."""
    return int(steps) % len(COMPASS_RING_ORDER)


def increment_ring_shift(current_steps: int) -> int:
    """Return UI state for one clockwise ring-shift click."""
    return int(current_steps) + 1


def decrement_ring_shift(current_steps: int) -> int:
    """Return UI state for one counter-clockwise ring-shift click."""
    return int(current_steps) - 1


def apply_ring_shift(chart: NatalChart, steps: int = 0) -> list[list[dict[str, Any]]]:
    """Shift the eight outer palaces around the Lo Shu compass ring.

    Positive steps move each canonical palace-star cell clockwise through:
    NW -> N -> NE -> E -> SE -> S -> SW -> W -> NW.

    The center palace remains fixed. No star values are recalculated and the
    canonical chart object is not mutated.
    """
    raw_steps = int(steps)
    normalized_steps = normalize_ring_shift(raw_steps)
    sector_map = chart.sector_map()
    output = _empty_display_grid()

    center_row, center_col = PALACE_TO_DISPLAY_INDEX["C"]
    center_sector = sector_map["C"]
    output[center_row][center_col] = {
        "display_position": DISPLAY_POSITIONS[center_row][center_col],
        "display_palace": "C",
        "canonical_palace": center_sector.position,
        "mountain": center_sector.mountain_star,
        "water": center_sector.water_star,
        "base": center_sector.base_star,
        "orientation_mode": "ring_shift",
        "rotation_applied": None,
        "ring_shift_steps": raw_steps,
        "normalized_ring_shift_steps": normalized_steps,
    }

    ring_size = len(COMPASS_RING_ORDER)
    for source_index, source_palace in enumerate(COMPASS_RING_ORDER):
        destination_palace = COMPASS_RING_ORDER[(source_index + normalized_steps) % ring_size]
        row_index, column_index = PALACE_TO_DISPLAY_INDEX[destination_palace]
        sector = sector_map[source_palace]
        output[row_index][column_index] = {
            "display_position": DISPLAY_POSITIONS[row_index][column_index],
            "display_palace": destination_palace,
            "canonical_palace": sector.position,
            "mountain": sector.mountain_star,
            "water": sector.water_star,
            "base": sector.base_star,
            "orientation_mode": "ring_shift",
            "rotation_applied": None,
            "ring_shift_steps": raw_steps,
            "normalized_ring_shift_steps": normalized_steps,
        }

    return _finalize_grid(output)


def palace_star_signature_from_chart(chart: NatalChart) -> set[tuple[str, int, int, int]]:
    """Return immutable palace-star combinations from the canonical chart."""
    return {
        (sector.position, sector.mountain_star, sector.water_star, sector.base_star)
        for sector in chart.sectors
    }


def palace_star_signature_from_grid(grid: list[list[dict[str, Any]]]) -> set[tuple[str, int, int, int]]:
    """Return immutable palace-star combinations from an oriented grid."""
    return {
        (cell["canonical_palace"], cell["mountain"], cell["water"], cell["base"])
        for row in grid
        for cell in row
    }


def assert_preserves_palace_star_assignments(chart: NatalChart, grid: list[list[dict[str, Any]]]) -> None:
    """Raise if an oriented grid changes any canonical palace-star assignment."""
    if palace_star_signature_from_chart(chart) != palace_star_signature_from_grid(grid):
        raise AssertionError("orientation changed palace-star assignments")
