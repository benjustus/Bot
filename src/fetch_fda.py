#!/usr/bin/env python3
"""Fetch FDA review priority (PRIORITY/STANDARD) + prior-approval count per event
from the free openFDA drugsfda API, matched by sponsor + action-date proximity.

review_priority is set at filing acceptance (months before the PDUFA date) -> it is
a legitimate POINT-IN-TIME feature (no look-ahead). Coverage is partial by nature:
openFDA holds US NDA/BLA originals, so novel small/mid-cap drugs match well while
supplement/label-expansion events (mostly big pharma) and foreign ADRs often don't.
Unmatched events are recorded as review_priority='' (NOT guessed).
"""
import requests, csv, json, time, re, sys
from pathlib import Path
UA = {'User-Agent': 'quant-research test@example.com'}
FDADIR = Path('data/fda'); FDADIR.mkdir(parents=True, exist_ok=True)

# ticker -> openFDA sponsor search token (first significant word of company name),
# with aliases for names that file under a different sponsor.
ALIAS = {
    'JNJ':'JANSSEN','ABBV':'ABBVIE','BMY':'BRISTOL','AZN':'ASTRAZENECA','GSK':'GLAXO',
    'NVS':'NOVARTIS','RHHBY':'GENENTECH','SNY':'SANOFI','LLY':'LILLY','PFE':'PFIZER',
    'MRK':'MERCK','GILD':'GILEAD','AMGN':'AMGEN','BIIB':'BIOGEN','REGN':'REGENERON',
    'VRTX':'VERTEX','TAK':'TAKEDA','NVO':'NOVO','BAYRY':'BAYER','TEVA':'TEVA',
    'IONS':'IONIS','IONI':'IONIS','ALNY':'ALNYLAM','MRNA':'MODERNA','BNTX':'BIONTECH',
}

def token(ticker, name):
    if ticker in ALIAS:
        return ALIAS[ticker]
    if not name:
        return None
    n = re.sub(r'[^A-Za-z ]', ' ', name).upper()
    stop = {'THE','INC','CORP','CORPORATION','LTD','LIMITED','PLC','CO','COMPANY','SA','NV','AG'}
    words = [w for w in n.split() if w not in stop and len(w) > 2]
    return words[0] if words else None

def fetch_sponsor(tok):
    fp = FDADIR / f'{tok}.json'
    if fp.exists():
        return json.loads(fp.read_text())
    try:
        r = requests.get('https://api.fda.gov/drug/drugsfda.json',
                         params={'search': f'sponsor_name:"{tok}"', 'limit': 100},
                         headers=UA, timeout=25)
        j = r.json(); res = j.get('results', [])
    except Exception:
        res = []
    time.sleep(0.4)
    subs = []
    for a in res:
        of = a.get('openfda', {})
        brand = (of.get('brand_name') or ['?'])[0]
        for s in a.get('submissions', []):
            if s.get('submission_status_date'):
                subs.append({'brand': brand, 'type': s.get('submission_type'),
                             'prio': s.get('review_priority'),
                             'status': s.get('submission_status'),
                             'date': s.get('submission_status_date')})
    fp.write_text(json.dumps(subs))
    return subs

def build():
    mc = {r['ticker']: r.get('name', '') for r in csv.DictReader(open('data/marketcap.csv'))}
    events = []
    for f in ['data/events_pdufa_bio.csv', 'data/events_regime_2022_2023.csv']:
        events += list(csv.DictReader(open(f)))
    out = []
    matched = 0
    for e in events:
        tk = e['ticker']; pd = e['pdufa_date'].replace('-', '')
        tok = token(tk, mc.get(tk, ''))
        prio = ''; prior = ''
        if tok:
            subs = fetch_sponsor(tok)
            # match ANY submission (ORIG or SUPPL) with a review_priority whose action
            # date is closest to the PDUFA date, within 30 days
            cand = [s for s in subs if s['prio'] and s['date'] and abs(int(s['date']) - int(pd)) <= 30]
            if cand:
                best = min(cand, key=lambda s: abs(int(s['date']) - int(pd)))
                prio = best['prio']; matched += 1
            # prior ORIG approvals by this sponsor strictly before the event (maturity proxy)
            prior = sum(1 for s in subs if s.get('type') == 'ORIG' and s['status'] == 'AP'
                        and s['date'] and int(s['date']) < int(pd))
        out.append({'ticker': tk, 'pdufa_date': e['pdufa_date'],
                    'review_priority': prio, 'prior_fda_approvals': prior})
    with open('data/fda_designations.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['ticker', 'pdufa_date', 'review_priority', 'prior_fda_approvals'])
        w.writeheader(); w.writerows(out)
    from collections import Counter
    print(f"events: {len(out)}  review_priority matched: {matched} ({matched/len(out)*100:.0f}%)")
    print("priority dist:", dict(Counter(r['review_priority'] or 'unmatched' for r in out)))

if __name__ == '__main__':
    build()
