"""Debug and ASCII rendering helpers for oriented overlay grids."""
from __future__ import annotations

from typing import Any


def ascii_rotated_display(grid: list[list[dict[str, Any]]], include_stars: bool = True) -> str:
    """Render an oriented grid with canonical palace labels and star triples."""
    lines = []
    for row in grid:
        parts = []
        for cell in row:
            display = cell.get("display_palace") or cell["display_position"]
            label = f"{cell['canonical_palace']}→{display}"
            if include_stars:
                label += f" [{cell['mountain']} {cell['water']} {cell['base']}]"
            parts.append(label)
        lines.append(" | ".join(parts))
    return "\n".join(lines)


def position_trace(grid: list[list[dict[str, Any]]]) -> list[dict[str, Any]]:
    """Return a flat trace of canonical palace to display position mappings."""
    return [cell.copy() for row in grid for cell in row]


def ascii_position_trace(grid: list[list[dict[str, Any]]]) -> str:
    """Render palace-to-display mappings for overlay debugging."""
    lines = []
    for cell in position_trace(grid):
        display = cell.get("display_palace") or cell["display_position"]
        mode = cell.get("orientation_mode", "matrix_rotation")
        if mode == "ring_shift":
            lines.append(
                f"[{cell['canonical_palace']}→{display}] "
                f"ring_shift={cell['ring_shift_steps']} "
                f"normalized={cell['normalized_ring_shift_steps']}"
            )
        else:
            lines.append(f"[{cell['canonical_palace']}→{display}] rotation={cell['rotation_applied']}°")
    return "\n".join(lines)
