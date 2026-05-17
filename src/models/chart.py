"""Natal chart model."""
from dataclasses import dataclass
from .sector import Sector

DISPLAY_ROWS = (("SE", "S", "SW"), ("E", "C", "W"), ("NE", "N", "NW"))
POSITION_ORDER = tuple(pos for row in DISPLAY_ROWS for pos in row)


@dataclass(frozen=True)
class NatalChart:
    period: int
    facing: str
    sectors: list[Sector]

    def sector_map(self) -> dict[str, Sector]:
        return {sector.position: sector for sector in self.sectors}

    def as_dict(self) -> dict:
        return {
            "period": self.period,
            "facing": self.facing,
            "grid": {sector.position: sector.as_dict() for sector in self.sectors},
        }

    def to_ascii(self) -> str:
        sectors = self.sector_map()
        lines = []
        for row in DISPLAY_ROWS:
            parts = []
            for pos in row:
                sector = sectors[pos]
                parts.append(f"{pos} [{sector.mountain_star} {sector.water_star} {sector.base_star}]")
            lines.append(" ".join(parts))
        return "\n".join(lines)
