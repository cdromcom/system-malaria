"""Fetch the single-record detail for every harvested association.

The list endpoint omits p_value, the confidence interval and the concept IDs; only
GET /v1/associations/{id} returns them. One request per finding.
"""
import json, os, pathlib, sys, time, requests
from dotenv import load_dotenv
load_dotenv("/Users/ppatel/system-public-challenge/.env")

CACHE = pathlib.Path("/Users/ppatel/system-public-challenge/cache")
S = requests.Session()
S.headers.update({"x-api-key": os.environ["SYSTEM_API_KEY"], "Accept": "application/json"})
BASE = "https://public-api.system.com/v1/associations"

ids = json.loads((CACHE / "evd_association_ids.json").read_text())
out, errs = {}, []
prev = CACHE / "stage5_detail.json"
if prev.exists():
    out = {d["system_id"]: d for d in json.loads(prev.read_text())}
    print(f"resuming with {len(out)} already cached")

for i, aid in enumerate(ids, 1):
    if aid in out:
        continue
    for attempt in range(6):
        r = S.get(f"{BASE}/{aid}", timeout=60)
        if r.status_code == 200:
            out[aid] = r.json(); break
        if r.status_code in (429, 500, 502, 503, 504):
            time.sleep(0.4 * (attempt + 1)); continue
        errs.append((aid, r.status_code)); break
    else:
        errs.append((aid, "gave up"))
    if i % 50 == 0:
        print(f"  {i}/{len(ids)}")
        (CACHE / "stage5_detail.json").write_text(json.dumps(list(out.values()), indent=1))

(CACHE / "stage5_detail.json").write_text(json.dumps(list(out.values()), indent=1))
has_p = sum(1 for d in out.values() if d.get("p_value") is not None)
has_ci = sum(1 for d in out.values() if d.get("ci_lower") is not None)
print(f"\n{len(out)} detail records, {len(errs)} failures")
print(f"  with a p-value             : {has_p} ({has_p/max(len(out),1):.0%})")
print(f"  with a confidence interval : {has_ci} ({has_ci/max(len(out),1):.0%})")
