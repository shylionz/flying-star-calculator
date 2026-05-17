"""Lookup-first Flying Star natal chart generator."""
from src.engine.lookup import get_lookup_chart
from src.engine.validator import validate_supported_case
from src.models.chart import NatalChart, POSITION_ORDER
from src.models.sector import Sector


def generate_natal_chart(period: int, facing: str, debug: bool = False) -> NatalChart:
    """Generate a natal chart from pre-validated lookup data only."""
    period, facing = validate_supported_case(period, facing)
    lookup_chart = get_lookup_chart(period, facing)
    if lookup_chart is None:  # Defensive; validator should catch this.
        raise ValueError(f"no lookup chart for P{period}/{facing}")

    sectors = []
    for position in POSITION_ORDER:
        mountain, water, base = lookup_chart[position]
        sectors.append(Sector(position, mountain, water, base))

    chart = NatalChart(period=period, facing=facing, sectors=sectors)
    if debug:
        print(f"Lookup hit: P{period}/{facing}")
        print(chart.to_ascii())
    return chart
