#!/usr/bin/env python3
"""Deterministically parse a saved pdufa.bio /decisions HTML page into a clean
events CSV. No model summarisation — pure regex over server-rendered rows.

Row format on the page:
  <a class="row" href="/fda-decision/VRTX-2025-01-30">
     <div class="t">VRTX · 2025-01-30 <span ...>✓</span></div>
     <div class="d"><span ...>Approved</span> — price-only</div></a>
"""
import re, csv, sys, html as _html
from pathlib import Path

ROW = re.compile(
    r'href="/fda-decision/([A-Z0-9.\-]+)-(\d{4}-\d{2}-\d{2})"'   # ticker, date (from URL)
    r'.*?<div class="d">(.*?)</div>',                              # outcome cell
    re.S,
)
TAG = re.compile(r'<[^>]+>')

def clean(s: str) -> str:
    return _html.unescape(TAG.sub(' ', s)).strip()

def parse(path: str):
    txt = Path(path).read_text()
    out = []
    for tick, date, dcell in ROW.findall(txt):
        cell = clean(dcell)
        low = cell.lower()
        if 'crl' in low or 'complete response' in low:
            outcome = 'CRL'
        elif 'approved' in low or 'approval' in low:
            outcome = 'Approved'
        elif 'delay' in low:
            outcome = 'Delayed'
        elif 'withdraw' in low:
            outcome = 'Withdrawn'
        else:
            outcome = 'Unknown'
        conf = 'source-verified' if 'source-verified' in low else (
               'price-only' if 'price-only' in low else 'other')
        out.append((tick, date, outcome, conf))
    # de-duplicate on (ticker, date, outcome) keeping first
    seen, dedup = set(), []
    for r in out:
        k = (r[0], r[1], r[2])
        if k in seen:
            continue
        seen.add(k); dedup.append(r)
    return dedup

if __name__ == '__main__':
    src = sys.argv[1] if len(sys.argv) > 1 else 'data/raw/pdufa_bio_decisions_2026-07-13.html'
    dst = sys.argv[2] if len(sys.argv) > 2 else 'data/events_pdufa_bio.csv'
    rows = parse(src)
    with open(dst, 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['ticker','pdufa_date','outcome','confidence']); w.writerows(rows)
    from collections import Counter
    print(f"parsed {len(rows)} unique events -> {dst}")
    print("by year:", dict(sorted(Counter(r[1][:4] for r in rows).items())))
    print("by outcome:", dict(Counter(r[2] for r in rows)))
    print("by confidence:", dict(Counter(r[3] for r in rows)))
