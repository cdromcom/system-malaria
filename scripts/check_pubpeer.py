"""Check every source paper for PubPeer comments, via the official PubPeer Foundation API.

Endpoint and payload shape are taken from The PubPeer Foundation's own browser extension,
published under the MIT licence at github.com/PubPeerFoundation/PubPeerBrowserExtensions
(`js/contentScript/pubpeer.js`):

    POST https://pubpeer.com/v3/publications?devkey=PubMed<Browser>
    Content-Type: application/json;charset=UTF-8
    {"version": "...", "browser": "...", "dois": [...] | "pmids": [...], "urls": [...]}
    -> {"status": "...", "feedbacks": [{id, title, total_comments, users, url, updates:[{type}]}]}

PubPeer returns a feedback record only for publications that have activity, so a paper absent
from the response has no PubPeer entry. Queried by DOI and again by PubMed ID, since a paper may
be indexed under either.

Polite: batches of 20, 2.5s apart, read-only.

    python3 -I scripts/check_pubpeer.py
"""
import collections
import json
import pathlib
import time

import requests

CACHE = pathlib.Path("/Users/ppatel/system-public-challenge/cache")
URL = "https://pubpeer.com/v3/publications?devkey=PubMedChrome"
H = {"Content-Type": "application/json;charset=UTF-8",
     "User-Agent": "malaria-evidence-audit/1.0 (research script; no contact configured)"}

papers = json.loads((CACHE / "integrity.json").read_text())
dois = sorted({(p.get("doi") or "").strip() for p in papers if p.get("doi")})
pmids = sorted({str(p["pubmed_id"]) for p in papers if p.get("pubmed_id")})
print(f"{len(papers)} papers: {len(dois)} DOIs, {len(pmids)} PubMed IDs")

feedbacks = {}


def query(key, values):
    out = []
    for i in range(0, len(values), 20):
        block = values[i:i + 20]
        body = {"version": "1.6.2", "browser": "Chrome", "urls": [], key: block}
        for attempt in range(3):
            try:
                r = requests.post(URL, json=body, headers=H, timeout=60)
            except requests.RequestException as e:
                print(f"  {type(e).__name__}, retrying")
                time.sleep(3 * (attempt + 1))
                continue
            if r.status_code == 200:
                out.extend(r.json().get("feedbacks") or [])
                break
            print(f"  HTTP {r.status_code}: {r.text[:120]}")
            time.sleep(3 * (attempt + 1))
        print(f"  {key}: {min(i + 20, len(values))}/{len(values)}, "
              f"{len(out)} feedbacks so far")
        time.sleep(2.5)
    return out


print("\nquerying by DOI")
for f in query("dois", dois):
    feedbacks[str(f.get("id", "")).lower()] = f
print("\nquerying by PubMed ID")
for f in query("pmids", pmids):
    feedbacks.setdefault(str(f.get("id", "")).lower(), f)

# Attach to our papers
out = []
for p in papers:
    hit = None
    for k in ((p.get("doi") or "").lower(), str(p.get("pubmed_id") or "")):
        if k and k in feedbacks:
            hit = feedbacks[k]
            break
    rec = {"pubmed_id": p.get("pubmed_id"), "doi": p.get("doi"),
           "on_pubpeer": bool(hit), "total_comments": 0, "update_types": [],
           "pubpeer_url": None, "n_commenters": 0, "title": None}
    if hit:
        types = [u.get("type") for u in (hit.get("updates") or []) if u.get("type")]
        users = [u.strip() for u in str(hit.get("users") or "").split(",") if u.strip()]
        rec.update({"total_comments": hit.get("total_comments") or 0,
                    "update_types": sorted(set(types)),
                    "pubpeer_url": hit.get("url"),
                    "n_commenters": len(users),
                    "title": hit.get("title")})
    out.append(rec)

(CACHE / "pubpeer.json").write_text(json.dumps(out, indent=1))

on = [r for r in out if r["on_pubpeer"]]
print(f"\n{len(on)} of {len(out)} papers have a PubPeer entry")
print(f"  with at least one comment : {sum(1 for r in on if r['total_comments'] > 0)}")
tc = collections.Counter(t for r in on for t in r["update_types"])
print(f"  update types across them  : {dict(tc) or 'none'}")
for r in sorted(on, key=lambda x: -x["total_comments"]):
    print(f"\n  PMID {r['pubmed_id']} | comments={r['total_comments']} | "
          f"commenters={r['n_commenters']} | {', '.join(r['update_types']) or 'no updates'}")
    print(f"     {(r['title'] or '')[:76]}")
    print(f"     {r['pubpeer_url']}")
if not on:
    print("\nNo source paper has any PubPeer entry.")
