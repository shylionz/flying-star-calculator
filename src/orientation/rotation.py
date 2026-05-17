"""Index-only 3x3 rotation mappings for visual chart presentation.

The canonical natal chart remains unchanged. These helpers only rearrange
matrix positions.
"""
from __future__ import annotations

from typing import Sequence, TypeVar

T = TypeVar("T")
Matrix3x3 = list[list[T]]

ORIENTATION_TO_DEGREES = {
    "top": 0,
    "right": 90,
    "bottom": 180,
    "left": 270,
}


def _validate_matrix(matrix: Sequence[Sequence[T]]) -> None:
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("rotation requires a 3x3 matrix")


def rotate_0(matrix: Sequence[Sequence[T]]) -> Matrix3x3[T]:
    """Return an unrotated copy of a 3x3 matrix."""
    _validate_matrix(matrix)
    return [[matrix[r][c] for c in range(3)] for r in range(3)]


def rotate_90(matrix: Sequence[Sequence[T]]) -> Matrix3x3[T]:
    """Return a 90-degree clockwise visual rotation."""
    _validate_matrix(matrix)
    return [[matrix[2 - c][r] for c in range(3)] for r in range(3)]


def rotate_180(matrix: Sequence[Sequence[T]]) -> Matrix3x3[T]:
    """Return a 180-degree visual rotation."""
    _validate_matrix(matrix)
    return [[matrix[2 - r][2 - c] for c in range(3)] for r in range(3)]


def rotate_270(matrix: Sequence[Sequence[T]]) -> Matrix3x3[T]:
    """Return a 270-degree clockwise / 90-degree counter-clockwise visual rotation."""
    _validate_matrix(matrix)
    return [[matrix[c][2 - r] for c in range(3)] for r in range(3)]


def rotation_degrees_for_orientation(orientation: str) -> int:
    """Map supported orientation names to clockwise rotation degrees."""
    key = orientation.strip().lower()
    if key not in ORIENTATION_TO_DEGREES:
        supported = ", ".join(ORIENTATION_TO_DEGREES)
        raise ValueError(f"unsupported orientation {orientation!r}; supported: {supported}")
    return ORIENTATION_TO_DEGREES[key]


def rotate_matrix(matrix: Sequence[Sequence[T]], orientation: str) -> Matrix3x3[T]:
    """Rotate a 3x3 matrix according to a display orientation."""
    degrees = rotation_degrees_for_orientation(orientation)
    if degrees == 0:
        return rotate_0(matrix)
    if degrees == 90:
        return rotate_90(matrix)
    if degrees == 180:
        return rotate_180(matrix)
    if degrees == 270:
        return rotate_270(matrix)
    raise AssertionError(f"unhandled rotation: {degrees}")
