#!/usr/bin/env python3
"""Yahoo Finance daily price fetcher with on-disk caching.

- Uses the public v8 chart endpoint (query1) which returns split-adjusted OHLC
  plus an adjclose series (split+dividend adjusted).
- Caches each ticker to data/prices/<TICKER>.csv so reruns never re-hit Yahoo.
- Delisted / unknown tickers are recorded in data/prices/_missing.txt so the
  survivorship gap is explicit and auditable (never silently dropped).
"""
import requests, csv, time, datetime as dt, os, sys
from pathlib import Path

PRICES_DIR = Path('data/prices')
PRICES_DIR.mkdir(parents=True, exist_ok=True)
MISSING = PRICES_DIR / '_missing.txt'
UA = {'User-Agent': 'Mozilla/5.0 (research; daily OHLC)'}

def _ts(d):
    return int(dt.datetime.strptime(d, '%Y-%m-%d').replace(tzinfo=dt.timezone.utc).timestamp())

def fetch_raw(ticker, start, end, tries=4):
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{ticker}'
    params = {'period1': _ts(start), 'period2': _ts(end), 'interval': '1d', 'events': 'split'}
    last = None
    for i in range(tries):
        try:
            r = requests.get(url, params=params, headers=UA, timeout=30)
            if r.status_code == 429:
                time.sleep(2 * (i + 1)); last = '429'; continue
            j = r.json()
            res = j.get('chart', {}).get('result')
            if not res:
                err = j.get('chart', {}).get('error', {})
                return None, (err.get('code') if err else 'empty')
            res = res[0]
            ts = res.get('timestamp', [])
            q = res['indicators']['quote'][0]
            adj = res['indicators'].get('adjclose', [{}])[0].get('adjclose')
            vol = q.get('volume')
            rows = []
            for k, t in enumerate(ts):
                d = dt.datetime.utcfromtimestamp(t).strftime('%Y-%m-%d')
                o, h, l, c = q['open'][k], q['high'][k], q['low'][k], q['close'][k]
                a = adj[k] if adj else c
                v = vol[k] if vol else None
                if c is None:
                    continue
                rows.append((d, o, h, l, c, a, v))
            return rows, None
        except Exception as e:
            last = str(e); time.sleep(1.5 * (i + 1))
    return None, last or 'fail'

def _covers(fp, start, end):
    """True if cached file's fetched-range (sidecar) covers [start,end]."""
    meta = fp.with_suffix('.range')
    if not meta.exists():
        return False
    try:
        fs, fe = meta.read_text().strip().split(',')
    except Exception:
        return False
    # allow 10d slack at the start (weekends/holidays/IPO) and require end within 6d
    s_ok = fs <= (dt.date.fromisoformat(start) + dt.timedelta(days=10)).isoformat()
    e_ok = fe >= (dt.date.fromisoformat(end) - dt.timedelta(days=6)).isoformat()
    return s_ok and e_ok

def get(ticker, start, end, polite=0.4):
    """Return cached rows for ticker, fetching+caching if needed. rows: list of
    (date,open,high,low,close,adjclose). Empty list means delisted/missing.
    Cache is range-aware: if the cached window does not cover [start,end] the
    ticker is re-fetched over the union range (prevents stale-narrow caches)."""
    fp = PRICES_DIR / f'{ticker}.csv'
    if fp.exists() and _covers(fp, start, end):
        with open(fp) as f:
            r = list(csv.reader(f))
        return [(x[0], *(float(v) if v not in ('', 'None') else None for v in x[1:])) for x in r[1:]]
    if fp.exists():
        # widen the request to the union so we only ever grow the cache
        meta = fp.with_suffix('.range')
        if meta.exists():
            try:
                fs, fe = meta.read_text().strip().split(',')
                start, end = min(start, fs), max(end, fe)
            except Exception:
                pass
    rows, err = fetch_raw(ticker, start, end)
    if polite:
        time.sleep(polite)
    fp.with_suffix('.range').write_text(f'{start},{end}')
    HDR = ['date','open','high','low','close','adjclose','volume']
    if rows is None or len(rows) == 0:
        with open(MISSING, 'a') as f:
            f.write(f'{ticker}\t{err}\n')
        # still write an empty cache marker to avoid re-fetching
        with open(fp, 'w', newline='') as f:
            csv.writer(f).writerow(HDR)
        return []
    with open(fp, 'w', newline='') as f:
        w = csv.writer(f); w.writerow(HDR); w.writerows(rows)
    return rows

if __name__ == '__main__':
    # quick self-test
    rows = get('ACAD', '2023-01-01', '2023-04-01')
    print('ACAD bars:', len(rows), 'sample:', rows[:2])
