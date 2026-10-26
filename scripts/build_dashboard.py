"""Build dashboard/data.json from air_data.csv.

Reads the daily AQICN snapshots collected by fetch_airdata.py and writes one
compact JSON file that the static dashboard in dashboard/ loads.

Usage:
    python scripts/build_dashboard.py
"""

import ast
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "air_data.csv"
TARGET = ROOT / "dashboard" / "data.json"


def parse_row(row):
    """Return (date, city, record) for one CSV row, or None if unusable."""
    try:
        pm25 = int(row["PM2.5"])
    except (TypeError, ValueError):
        return None

    record = {"pm25": pm25, "aqi": int(row["AQI"])}
    try:
        payload = ast.literal_eval(row["JSON"])
        iaqi = payload.get("iaqi", {})
        for key, name in (("t", "temp"), ("h", "humidity"), ("w", "wind")):
            if key in iaqi:
                record[name] = iaqi[key]["v"]
        record["station"] = payload.get("city", {}).get("name")
    except (ValueError, SyntaxError):
        pass

    day = row["Timestamp"][:10]
    return day, row["City"], record


def build():
    cities = {}
    with SOURCE.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            parsed = parse_row(row)
            if parsed is None:
                continue
            day, city, record = parsed
            # One snapshot per city per day; keep the latest if a day repeats.
            cities.setdefault(city, {})[day] = record

    series = {}
    stations = {}
    for city, days in cities.items():
        ordered = sorted(days.items())
        series[city] = [
            [day, rec["pm25"], rec.get("temp"), rec.get("humidity"), rec.get("wind")]
            for day, rec in ordered
        ]
        stations[city] = ordered[-1][1].get("station")

    data = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "fields": ["date", "pm25_aqi", "temp_c", "humidity_pct", "wind"],
        "stations": stations,
        "series": series,
    }
    TARGET.parent.mkdir(exist_ok=True)
    TARGET.write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")
    total = sum(len(v) for v in series.values())
    print(f"Wrote {TARGET.relative_to(ROOT)}: {total} city-days across {len(series)} cities")


if __name__ == "__main__":
    build()
