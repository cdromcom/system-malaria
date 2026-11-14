"""Query retractionrisk.com for Retraction Watch status and Altmetric (Bluesky/X) attention.

RetractionRisk Scanner (The Unreliable Science Project, maintained by Er-Te Zheng, funded by
EMIF) aggregates Crossref, OpenAlex, Retraction Watch, Altmetric, Bluesky and PubPeer.

What this adds over scripts/check_integrity.py: the Retraction Watch status string, and counts
plus sentiment of critical social-media attention, which no other source here provides.

What it cannot add: PubPeer comment counts. Their backend reaches PubPeer from a cloud IP and
gets a 403, which is why their own front end fetches PubPeer in the visitor's browser and posts
the result up. Called server-side like this, `stats.pubpeer` is always 0.

Polite: one request at a time, 2s apart, generic User-Agent, no contact address sent.

    python3 -I scripts/check_retractionrisk.py
"""
import collections
import json
import pathlib
import time

import requests

CACHE = pathlib.Path("/Users/ppatel/system-public-challenge/cache")
UA = {"User-Agent": "malaria-evidence-audit/1.0 (research script; no contact configured)",
      "Content-Type": "application/json"}
URL = "https://www.retractionrisk.com/api/search"

integ = json.loads((CACHE / "integrity.json").read_text())
dois = sorted({r["doi"] for r in integ if r.get("doi")})
print(f"{len(dois)} DOIs to query")

out = {}
prev = CACHE / "retractionrisk.json"
if prev.exists():
    out = {d["doi"]: d for d in json.loads(prev.read_text())}
    print(f"resuming with {len(out)} cached")

for i, doi in enumerate(dois, 1):
    if doi in out:
        continue
    rec = {"doi": doi, "ok": False}
    for attempt in range(3):
        try:
            r = requests.post(URL, json={"doi": doi}, headers=UA, timeout=60)
        except requests.RequestException as e:
            time.sleep(2 * (attempt + 1))
            rec["error"] = f"{type(e).__name__}"
            continue
        if r.status_code != 200:
            rec["error"] = f"HTTP {r.status_code}"
            time.sleep(2 * (attempt + 1))
            continue
        try:
            d = r.json()
        except ValueError:
            rec["error"] = "non-JSON response"
            break
        if d.get("error"):
            rec["error"] = d["error"]
            break
        st = d.get("stats") or {}
        md = d.get("metadata") or {}
        rl = d.get("retractionLike") or {}
        posts = d.get("posts") or []
        rec.update({
            "ok": True,
            "rw_status": md.get("status"),
            "rw_status_note": md.get("statusNote"),
            "rw_status_date": md.get("statusDate"),
            "title": md.get("title"),
            "total_posts": st.get("total"), "bluesky": st.get("bluesky"),
            "x": st.get("x"), "x_negative": st.get("xNegative"),
            "pubpeer": st.get("pubpeer"), "has_risk": st.get("hasRisk"),
            "risk_count": st.get("riskCount"), "has_sleuth": st.get("hasSleuth"),
            "retraction_like_in_scope": rl.get("inScope"),
            "retraction_like_reason": rl.get("reason"),
            "negative_posts": [
                {"platform": p.get("platformName"), "sentiment": p.get("sentimentLabel"),
                 "date": p.get("date"), "url": p.get("url"), "is_sleuth": p.get("isSleuth")}
                for p in posts
                if str(p.get("sentimentLabel", "")).lstrip("-").isdigit()
                and str(p.get("sentimentLabel", "")).startswith("-")],
            "n_posts_returned": len(posts),
        })
        break
    out[doi] = rec
    if i % 10 == 0:
        print(f"  {i}/{len(dois)}")
        (CACHE / "retractionrisk.json").write_text(json.dumps(list(out.values()), indent=1))
    time.sleep(2.0)

(CACHE / "retractionrisk.json").write_text(json.dumps(list(out.values()), indent=1))

ok = [r for r in out.values() if r.get("ok")]
print(f"\n{len(ok)} of {len(dois)} queried successfully")
print("\nRetraction Watch status:")
for k, v in collections.Counter(r.get("rw_status") for r in ok).most_common():
    print(f"  {str(k):28s} {v}")
risky = [r for r in ok if r.get("has_risk")]
print(f"\nflagged as carrying risk       : {len(risky)}")
print(f"with any Bluesky post          : {sum(1 for r in ok if (r.get('bluesky') or 0) > 0)}")
print(f"with any negative X post       : {sum(1 for r in ok if (r.get('x_negative') or 0) > 0)}")
print(f"with a sleuth-authored post    : {sum(1 for r in ok if r.get('has_sleuth'))}")
print(f"pubpeer counts returned > 0    : {sum(1 for r in ok if (r.get('pubpeer') or 0) > 0)}"
      "   (expected 0 — server-side calls get a 403 from PubPeer)")
print("\npapers with critical attention:")
for r in sorted(ok, key=lambda x: -(x.get("risk_count") or 0)):
    if r.get("has_risk") or (r.get("x_negative") or 0) or (r.get("bluesky") or 0):
        print(f"  [{r.get('rw_status')}] risk={r.get('risk_count')} "
              f"bluesky={r.get('bluesky')} xneg={r.get('x_negative')} "
              f"sleuth={r.get('has_sleuth')}  {str(r.get('title'))[:62]}")
