"""Input validation for lookup-first Flying Star calculator."""
from .lookup import supported_cases


def normalize_facing(facing: str) -> str:
    if not isinstance(facing, str) or not facing.strip():
        raise ValueError("facing must be a non-empty string")
    return facing.strip().upper()


def validate_period(period: int) -> int:
    try:
        parsed = int(period)
    except (TypeError, ValueError) as exc:
        raise ValueError("period must be an integer") from exc
    if parsed < 1 or parsed > 9:
        raise ValueError("period must be between 1 and 9")
    return parsed


def validate_supported_case(period: int, facing: str) -> tuple[int, str]:
    parsed_period = validate_period(period)
    parsed_facing = normalize_facing(facing)
    if (parsed_period, parsed_facing) not in supported_cases():
        supported = ", ".join(f"P{p}/{f}" for p, f in supported_cases())
        raise ValueError(f"unsupported validated case P{parsed_period}/{parsed_facing}; supported: {supported}")
    return parsed_period, parsed_facing
