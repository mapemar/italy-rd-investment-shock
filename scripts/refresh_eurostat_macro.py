#!/usr/bin/env python3
"""Download Eurostat national R&D intensity and GDP series for Italy.

The script preserves Eurostat observation flags and dataset update metadata.
It does not impute missing observations or construct an R&D-specific deflator.
"""
from __future__ import annotations
import csv, json, os, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
OUT = Path("data/processed")
START, END = 2010, 2024
HEADERS = ["dataset","geo","year","dimension","category_code","category_label","unit","value","flag","dataset_updated","extracted_at_utc","source_url"]

def get_json(dataset: str, params: dict) -> tuple[dict, str]:
    query = urllib.parse.urlencode({"lang":"en", **params})
    url = f"{BASE}{dataset}?{query}"
    req = urllib.request.Request(url, headers={"User-Agent":"italy-rd-investment-shock research/1.0"})
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.load(response), url

def unpack(js: dict, dataset: str, source_url: str, dimension: str, unit: str) -> list[dict]:
    ids, sizes = js["id"], js["size"]
    dims = js["dimension"]
    indexes = [dims[k]["category"]["index"] for k in ids]
    labels = [dims[k]["category"].get("label", {}) for k in ids]
    time_pos = ids.index("time")
    cat_pos = ids.index(dimension) if dimension in ids else None
    geo_pos = ids.index("geo")
    n = 1
    strides = []
    for size in reversed(sizes):
        strides.insert(0, n)
        n *= size
    out=[]
    for key, value in js.get("value", {}).items():
        flat=int(key); coords=[(flat//strides[i])%sizes[i] for i in range(len(sizes))]
        year_code=list(indexes[time_pos].keys())[list(indexes[time_pos].values()).index(coords[time_pos])]
        if not (START <= int(year_code) <= END): continue
        geo_code=list(indexes[geo_pos].keys())[list(indexes[geo_pos].values()).index(coords[geo_pos])]
        cat_code=""
        cat_label=""
        if cat_pos is not None:
            cat_code=list(indexes[cat_pos].keys())[list(indexes[cat_pos].values()).index(coords[cat_pos])]
            cat_label=labels[cat_pos].get(cat_code,cat_code)
        flags=js.get("status",{}).get(key,"")
        out.append({"dataset":dataset,"geo":geo_code,"year":year_code,"dimension":dimension,
          "category_code":cat_code,"category_label":cat_label,"unit":unit,"value":value,
          "flag":flags,"dataset_updated":js.get("updated",""),"extracted_at_utc":datetime.now(timezone.utc).isoformat(),
          "source_url":source_url})
    return out

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    rows=[]
    # Harmonised GERD intensity: total and each sector of performance.
    for sector in ["TOTAL","BES","GOV","HES","PNP"]:
        js,url=get_json("rd_e_gerdtot",{"freq":"A","unit":"PC_GDP","geo":"IT","sectperf":sector,
            "sinceTimePeriod":str(START),"untilTimePeriod":str(END)})
        rows += unpack(js,"rd_e_gerdtot",url,"sectperf","PC_GDP")
    with (OUT/"eurostat_rd_intensity_italy_2010_2024.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=HEADERS);w.writeheader();w.writerows(rows)

    # GDP: current-price level and chain-linked volume index. GDP deflator is
    # computed downstream as a proxy; it is not an R&D-specific price index.
    gdp_rows=[]
    for unit_code in ["CP_MEUR","CLV_I20"]:
        js,url=get_json("nama_10_gdp",{"freq":"A","unit":unit_code,"geo":"IT","na_item":"B1GQ",
            "sinceTimePeriod":str(START),"untilTimePeriod":str(END)})
        gdp_rows += unpack(js,"nama_10_gdp",url,"na_item",unit_code)
    with (OUT/"eurostat_gdp_italy_2010_2024.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=HEADERS);w.writeheader();w.writerows(gdp_rows)
    print(f"Saved {len(rows)} GERD intensity observations and {len(gdp_rows)} GDP observations (expected up to {2*(END-START+1)}).")
    if len(rows) == 0 or len(gdp_rows) == 0:
        raise RuntimeError("Eurostat returned an empty core series; refusing to publish empty datasets.")

if __name__ == "__main__":
    main()
