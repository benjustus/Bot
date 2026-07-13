#!/usr/bin/env python3
import csv, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, 'src')
import yahoo

def load_events(fp):
    with open(fp) as f:
        return list(csv.DictReader(f))

def main(events_fp, start, end):
    evs = load_events(events_fp)
    tickers = sorted({e['ticker'] for e in evs})
    print(f'{len(evs)} events, {len(tickers)} unique tickers')
    ok = miss = 0
    for i, t in enumerate(tickers):
        rows = yahoo.get(t, start, end)
        if rows:
            ok += 1
        else:
            miss += 1
        if (i + 1) % 25 == 0:
            print(f'  {i+1}/{len(tickers)}  priceable={ok} missing={miss}')
    print(f'DONE tickers: priceable={ok} missing={miss} ({miss/len(tickers)*100:.1f}% delisted/unknown)')
    # benchmarks
    for b in ['XBI', '^GSPC', 'IBB']:
        r = yahoo.get(b, start, end)
        print(f'benchmark {b}: {len(r)} bars')

if __name__ == '__main__':
    main('data/events_pdufa_bio.csv', '2024-07-01', '2026-07-27')
