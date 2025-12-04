#!/usr/bin/env python3
"""
Download Brazil states GeoJSON and save to web/brazil-states.geojson
Run: python3 scripts/fetch_geojson.py
"""
import pathlib
import sys

try:
    import requests
except Exception as e:
    print("Missing dependency 'requests'. Install with: pip install -r requirements.txt")
    raise

URL = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "web" / "brazil-states.geojson"

OUT.parent.mkdir(parents=True, exist_ok=True)

print(f"Downloading GeoJSON from {URL} ...")
resp = requests.get(URL, timeout=120)
resp.raise_for_status()

print(f"Writing {OUT} ({len(resp.content)} bytes)")
OUT.write_bytes(resp.content)
print("Done.")
