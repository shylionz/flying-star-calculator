from __future__ import annotations

"""Command-line interface for the lookup-first Flying Star calculator."""
import argparse
import json
import sys

from src.engine.base_chart import generate_natal_chart
from src.orientation.debug import ascii_position_trace, ascii_rotated_display
from src.orientation.transform import apply_ring_shift, oriented_grid


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Flying Star natal chart calculator (validated lookup cases only)")
    parser.add_argument("--period", type=int, required=True, help="Flying Star period, 1-9")
    parser.add_argument("--facing", required=True, help="Facing direction, e.g. SE, N1, SW2")
    parser.add_argument("--format", choices=("ascii", "json"), default="ascii", help="Output format")
    parser.add_argument("--debug", action="store_true", help="Print lookup debug details")
    parser.add_argument("--orientation", choices=("top", "right", "bottom", "left"), help="Matrix-rotation overlay orientation")
    parser.add_argument("--ring-shift", type=int, help="Compass ring shift steps; positive is clockwise, negative is counter-clockwise")
    parser.add_argument("--trace", action="store_true", help="Print orientation palace-to-position trace")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.orientation is not None and args.ring_shift is not None:
        print("ERROR: choose either --orientation matrix rotation or --ring-shift, not both", file=sys.stderr)
        return 2

    try:
        chart = generate_natal_chart(args.period, args.facing, debug=args.debug)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.ring_shift is not None:
        grid = apply_ring_shift(chart, args.ring_shift)
        if args.format == "json":
            print(json.dumps({"period": chart.period, "facing": chart.facing, "orientation_mode": "ring_shift", "ring_shift": args.ring_shift, "grid": grid}, indent=2))
        else:
            print(ascii_rotated_display(grid))
            if args.trace:
                print()
                print(ascii_position_trace(grid))
    elif args.orientation:
        grid = oriented_grid(chart, args.orientation)
        if args.format == "json":
            print(json.dumps({"period": chart.period, "facing": chart.facing, "orientation_mode": "matrix_rotation", "orientation": args.orientation, "grid": grid}, indent=2))
        else:
            print(ascii_rotated_display(grid))
            if args.trace:
                print()
                print(ascii_position_trace(grid))
    elif args.format == "json":
        print(json.dumps(chart.as_dict(), indent=2))
    elif not args.debug:
        print(chart.to_ascii())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
