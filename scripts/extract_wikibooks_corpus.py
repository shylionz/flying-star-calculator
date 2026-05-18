#!/usr/bin/env python3
"""Extract Flying Star validation corpus from Wikibooks period pages.

Reference format notes:
- Pages list charts as 3x3 numeric grids with South on top.
- Cell positions are SE,S,SW / E,C,W / NE,N,NW.
- Wikibooks cell notation is <sup>A</sup>B<sup>C</sup>.
- Normalize as mountain=A, base=B, water=C; app stores {mountain, water, base}.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
RESEARCH_DIR = ROOT / "research"
VALIDATION_DIR = ROOT / "validation"
UI_CHARTS = ROOT / "ui" / "data" / "charts.json"
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "master_validation.json"
LOOKUP_PATH = ROOT / "src" / "engine" / "lookup.py"

POSITIONS = ["SE", "S", "SW", "E", "C", "W", "NE", "N", "NW"]
ALL_FACINGS = [
    "N1", "N2", "N3", "NE1", "NE2", "NE3", "E1", "E2", "E3", "SE1", "SE2", "SE3",
    "S1", "S2", "S3", "SW1", "SW2", "SW3", "W1", "W2", "W3", "NW1", "NW2", "NW3",
]
SOURCE_URL = "https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_{period}"
CHART_HEADER = re.compile(
    r"The Flying Star Chart for Period\s*=\s*(?P<period>[1-9])\s*,\s*"
    r"Mountain Direction\s*=\s*(?P<mountain>[A-Z]{1,2}[123])\s*,?\s*and\s*"
    r"Facing Direction\s*=\s*(?P<facing>[A-Z]{1,2}[123])",
    re.IGNORECASE,
)
GRID_CELL = re.compile(r"^[1-9]{3}$")


def fetch_period_text(period: int, cache: bool = True) -> str:
    RESEARCH_DIR.mkdir(exist_ok=True)
    raw_path = RESEARCH_DIR / f"wikibooks_period{period}.txt"
    if cache and raw_path.exists():
        return raw_path.read_text(encoding="utf-8")
    url = SOURCE_URL.format(period=period)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 FlyingStarValidation/1.0 (research extraction)"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text("\n")
    raw_path.write_text(text, encoding="utf-8")
    return text


def parse_period(period: int, text: str) -> list[dict[str, Any]]:
    lines = [line.strip().replace("\xa0", " ") for line in text.splitlines()]
    cases: list[dict[str, Any]] = []
    idx = 0
    while idx < len(lines):
        match = CHART_HEADER.search(lines[idx])
        if not match:
            idx += 1
            continue
        header_period = int(match.group("period"))
        mountain = match.group("mountain").upper()
        facing = match.group("facing").upper()
        digit_tokens: list[str] = []
        probe = idx + 1
        while probe < len(lines) and len(digit_tokens) < 27:
            candidate = lines[probe].strip()
            if CHART_HEADER.search(candidate):
                break
            if GRID_CELL.match(candidate):
                digit_tokens.extend(candidate)
            elif re.match(r"^[1-9]$", candidate):
                digit_tokens.append(candidate)
            probe += 1
        cells = ["".join(digit_tokens[i:i + 3]) for i in range(0, min(len(digit_tokens), 27), 3)]
        grid = {}
        if header_period == period and len(cells) == 9 and all(GRID_CELL.match(cell) for cell in cells):
            for position, raw in zip(POSITIONS, cells):
                mountain_star, base, water = (int(raw[0]), int(raw[1]), int(raw[2]))
                grid[position] = {"mountain": mountain_star, "water": water, "base": base, "raw": raw}
        cases.append({
            "id": f"P{period:01d}-{facing}",
            "period": header_period,
            "facing": facing,
            "mountain": mountain,
            "source": "Wikibooks Flying Star Feng Shui period page",
            "source_url": SOURCE_URL.format(period=period),
            "validation_status": "extracted",
            "validation_notes": "Extracted from Wikibooks period chart. Raw <sup>A</sup>B<sup>C</sup> cells normalized to app format as mountain=A, water=C, base=B.",
            "position_order": POSITIONS,
            "grid": {p: {k: v for k, v in cell.items() if k != "raw"} for p, cell in grid.items()},
            "raw_cells": dict(zip(POSITIONS, cells)),
        })
        idx = probe
    return cases


def audit_cases(cases: list[dict[str, Any]], period: int) -> dict[str, Any]:
    keys = [(case.get("period"), case.get("facing")) for case in cases]
    counts = Counter(keys)
    duplicate_keys = [f"P{p}/{f}" for (p, f), count in counts.items() if count > 1]
    malformed = []
    for case in cases:
        errors = []
        if case.get("period") != period:
            errors.append("period_mismatch")
        if case.get("facing") not in ALL_FACINGS:
            errors.append("invalid_facing")
        grid = case.get("grid", {})
        if sorted(grid.keys()) != sorted(POSITIONS):
            errors.append("missing_or_extra_positions")
        for position in POSITIONS:
            cell = grid.get(position)
            if not isinstance(cell, dict):
                errors.append(f"{position}:missing_cell")
                continue
            for field in ("mountain", "water", "base"):
                value = cell.get(field)
                if not isinstance(value, int) or value < 1 or value > 9:
                    errors.append(f"{position}:{field}_invalid")
        if errors:
            malformed.append({"id": case.get("id"), "period": case.get("period"), "facing": case.get("facing"), "errors": errors})
    grids_by_key: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for case in cases:
        grids_by_key[(case.get("period"), case.get("facing"))].append(case.get("grid"))
    conflicts = []
    for key, grids in grids_by_key.items():
        if len({json.dumps(grid, sort_keys=True) for grid in grids}) > 1:
            conflicts.append(f"P{key[0]}/{key[1]}")
    missing_facings = sorted(set(ALL_FACINGS) - {case.get("facing") for case in cases}, key=ALL_FACINGS.index)
    extra_facings = sorted({case.get("facing") for case in cases} - set(ALL_FACINGS))
    return {
        "period": period,
        "extracted_count": len(cases),
        "expected_count": 24,
        "duplicate_count": sum(count - 1 for count in counts.values() if count > 1),
        "duplicate_keys": duplicate_keys,
        "malformed_count": len(malformed),
        "malformed": malformed,
        "conflicts": conflicts,
        "missing_facings": missing_facings,
        "extra_facings": extra_facings,
        "sample_object": cases[0] if cases else None,
    }


def strip_raw(case: dict[str, Any]) -> dict[str, Any]:
    cleaned = dict(case)
    cleaned.pop("raw_cells", None)
    return cleaned


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_existing_charts() -> dict[str, Any]:
    """Load the pre-extraction app dataset for conflict audit.

    Prefer git HEAD so a failed/partial local write cannot contaminate the
    conflict evidence. Fall back to the working tree when HEAD is unavailable.
    """
    import subprocess

    try:
        raw = subprocess.check_output(["git", "show", "HEAD:ui/data/charts.json"], cwd=ROOT, stderr=subprocess.DEVNULL)
        return json.loads(raw.decode("utf-8"))
    except Exception:
        if not UI_CHARTS.exists():
            return {"charts": {}}
        return json.loads(UI_CHARTS.read_text(encoding="utf-8"))


def compare_existing(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    existing = load_existing_charts().get("charts", {})
    conflicts = []
    for case in cases:
        key = f"{case['period']}|{case['facing']}"
        current = existing.get(key)
        if current and current.get("grid") != case.get("grid"):
            conflicts.append({"key": key, "existing": current.get("grid"), "extracted": case.get("grid")})
    return conflicts


def build_charts_json(cases: list[dict[str, Any]]) -> dict[str, Any]:
    charts = {}
    for case in sorted(cases, key=lambda c: (c["period"], ALL_FACINGS.index(c["facing"]))):
        key = f"{case['period']}|{case['facing']}"
        charts[key] = {"period": case["period"], "facing": case["facing"], "grid": case["grid"]}
    return {
        "description": "Full 216-case Flying Star chart dataset extracted from Wikibooks period pages; lookup/reference only.",
        "version": "1.0-full-wikibooks-extraction",
        "created_date": str(date.today()),
        "total_cases": len(charts),
        "source_method": "Direct extraction from Wikibooks Period 1-9 Flying Star charts. Raw <sup>A</sup>B<sup>C</sup> cells normalized as mountain=A, water=C, base=B.",
        "position_order": POSITIONS,
        "charts": charts,
    }


def build_lookup_py(charts_data: dict[str, Any]) -> str:
    entries = []
    for key, chart in charts_data["charts"].items():
        period_s, facing = key.split("|")
        positions = []
        for pos in POSITIONS:
            cell = chart["grid"][pos]
            positions.append(f'"{pos}": ({cell["mountain"]}, {cell["water"]}, {cell["base"]})')
        entries.append(f'    ({period_s}, "{facing}"): {{{", ".join(positions)}}},')
    return """from __future__ import annotations\n\n\"\"\"Pre-validated lookup tables for Flying Star Calculator.\n\nFull 216-case dataset extracted from Wikibooks period chart pages.\nDO NOT derive from formulas alone - use lookup-first reference data.\n\"\"\"\n\nNATAL_CHART_LOOKUP = {\n""" + "\n".join(entries) + "\n}\n\n\ndef get_lookup_chart(period: int, facing: str) -> dict | None:\n    \"\"\"Return position -> (mountain, water, base), or None if unsupported.\"\"\"\n    return NATAL_CHART_LOOKUP.get((period, facing.upper()))\n\n\ndef supported_cases() -> list[tuple[int, str]]:\n    \"\"\"Return supported validated (period, facing) cases.\"\"\"\n    return sorted(NATAL_CHART_LOOKUP.keys())\n"


def write_report(period_audits: list[dict[str, Any]], full_audit: dict[str, Any], existing_conflicts: list[dict[str, Any]]) -> None:
    lines = [
        "# Full Validation Corpus Extraction Audit",
        "",
        f"Date: {date.today()}",
        "",
        "Source: Wikibooks Flying Star Feng Shui Period 1-9 pages.",
        "Normalization: raw Wikibooks cell `<sup>A</sup>B<sup>C</sup>` => mountain=A, water=C, base=B; app stores `{mountain, water, base}`.",
        "",
        "## Period audits",
        "",
    ]
    for audit in period_audits:
        path = RESEARCH_DIR / f"corpus_period{audit['period']}.json"
        size = path.stat().st_size if path.exists() else 0
        sample = json.dumps(audit["sample_object"], ensure_ascii=False, indent=2) if audit.get("sample_object") else "null"
        lines.extend([
            f"### Period {audit['period']}",
            "",
            f"- extracted count: {audit['extracted_count']}",
            f"- duplicate count: {audit['duplicate_count']}",
            f"- malformed count: {audit['malformed_count']}",
            f"- conflicts: {audit['conflicts'] or []}",
            f"- missing facings: {audit['missing_facings'] or []}",
            f"- file path: `{path.relative_to(ROOT)}`",
            f"- file size: {size} bytes",
            "- one sample object:",
            "",
            "```json",
            sample,
            "```",
            "",
        ])
    lines.extend([
        "## Full merge audit",
        "",
        f"- total extracted count: {full_audit['total_count']}",
        f"- expected count: {full_audit['expected_count']}",
        f"- unique key count: {full_audit['unique_key_count']}",
        f"- duplicate count: {full_audit['duplicate_count']}",
        f"- malformed count: {full_audit['malformed_count']}",
        f"- missing keys: {full_audit['missing_keys'] or []}",
        f"- existing dataset conflicts: {len(existing_conflicts)}",
        f"- existing conflict keys: {[item['key'] for item in existing_conflicts]}",
        f"- merged corpus path: `{(VALIDATION_DIR / 'full_validation_corpus.json').relative_to(ROOT)}`",
        f"- merged corpus size: {(VALIDATION_DIR / 'full_validation_corpus.json').stat().st_size if (VALIDATION_DIR / 'full_validation_corpus.json').exists() else 0} bytes",
        "",
    ])
    write_path = VALIDATION_DIR / "full_validation_extraction_audit.md"
    write_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--period", type=str, default="all", help="1-9 or all")
    parser.add_argument("--no-cache", action="store_true")
    parser.add_argument("--write-app", action="store_true", help="Update ui/data/charts.json, lookup.py, and tests fixture")
    args = parser.parse_args()

    periods = list(range(1, 10)) if args.period == "all" else [int(args.period)]
    all_cases: list[dict[str, Any]] = []
    period_audits = []
    for period in periods:
        text = fetch_period_text(period, cache=not args.no_cache)
        cases = parse_period(period, text)
        audit = audit_cases(cases, period)
        period_payload = {
            "description": f"Extracted validation corpus for Flying Star Period {period}",
            "period": period,
            "source_url": SOURCE_URL.format(period=period),
            "position_order": POSITIONS,
            "audit": audit,
            "test_cases": [strip_raw(case) for case in cases],
        }
        write_json(RESEARCH_DIR / f"corpus_period{period}.json", period_payload)
        all_cases.extend(strip_raw(case) for case in cases)
        period_audits.append(audit)

    if args.period == "all":
        keys = [(case["period"], case["facing"]) for case in all_cases]
        counts = Counter(keys)
        expected_keys = {(period, facing) for period in range(1, 10) for facing in ALL_FACINGS}
        actual_keys = set(keys)
        malformed_count = sum(audit["malformed_count"] for audit in period_audits)
        full_audit = {
            "total_count": len(all_cases),
            "expected_count": 216,
            "unique_key_count": len(actual_keys),
            "duplicate_count": sum(count - 1 for count in counts.values() if count > 1),
            "malformed_count": malformed_count,
            "missing_keys": [f"P{p}/{f}" for p, f in sorted(expected_keys - actual_keys)],
        }
        full_payload = {
            "description": "Full 216-case validation corpus for Flying Star Calculator. Lookup/reference only; no formula derivation.",
            "version": "1.0-full-wikibooks-extraction",
            "created_date": str(date.today()),
            "total_cases": len(all_cases),
            "source_method": "Direct extraction from Wikibooks Period 1-9 Flying Star charts. Raw <sup>A</sup>B<sup>C</sup> cells normalized as mountain=A, water=C, base=B.",
            "position_order": POSITIONS,
            "audit": full_audit,
            "test_cases": all_cases,
        }
        write_json(VALIDATION_DIR / "full_validation_corpus.json", full_payload)
        existing_conflicts = compare_existing(all_cases)
        write_report(period_audits, full_audit, existing_conflicts)
        if args.write_app:
            charts_data = build_charts_json(all_cases)
            write_json(UI_CHARTS, charts_data)
            write_json(FIXTURE_PATH, full_payload)
            LOOKUP_PATH.write_text(build_lookup_py(charts_data), encoding="utf-8")
        print(json.dumps({"period_audits": period_audits, "full_audit": full_audit, "existing_conflict_count": len(existing_conflicts)}, indent=2))
    else:
        print(json.dumps(period_audits[0], indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
