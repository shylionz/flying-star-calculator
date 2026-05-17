"""Sector model for a Flying Star natal chart."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Sector:
    position: str
    mountain_star: int
    water_star: int
    base_star: int

    def as_dict(self) -> dict:
        return {
            "position": self.position,
            "mountain": self.mountain_star,
            "water": self.water_star,
            "base": self.base_star,
        }
