#!/usr/bin/env python3
"""Fetch CURRENT market cap + shares outstanding via Yahoo v7 quote (crumb flow).
NOTE: this is the *current* value (query date), used only as a coarse-tier proxy
for the historical size bucket. Documented as an approximation, not point-in-time.
"""
import requests, csv, json, time, sys
from pathlib import Path
UA={'User-Agent':'Mozilla/5.0'}

def session_crumb():
    s=requests.Session(); s.headers.update(UA)
    try: s.get('https://fc.yahoo.com',timeout=15)
    except Exception: pass
    c=s.get('https://query1.finance.yahoo.com/v1/test/getcrumb',timeout=15).text.strip()
    return s,c

def fetch(symbols):
    s,crumb=session_crumb()
    out={}
    for i in range(0,len(symbols),40):
        batch=symbols[i:i+40]
        url='https://query1.finance.yahoo.com/v7/finance/quote'
        r=s.get(url,params={'symbols':','.join(batch),'crumb':crumb},timeout=25)
        try: res=r.json().get('quoteResponse',{}).get('result',[])
        except Exception: res=[]
        for q in res:
            out[q.get('symbol')]={'marketCap':q.get('marketCap'),
                                  'shares':q.get('sharesOutstanding'),
                                  'name':q.get('longName') or q.get('shortName'),
                                  'price':q.get('regularMarketPrice')}
        time.sleep(0.6)
    return out

def tier(mc):
    if mc is None: return 'n/a'
    b=mc/1e9
    if b<0.5: return '<500M'
    if b<2:   return '500M-2B'
    if b<10:  return '2-10B'
    return '>10B'

if __name__=='__main__':
    tickers=set()
    for fp in ['data/events_pdufa_bio.csv','data/events_original16.csv']:
        if Path(fp).exists():
            tickers|={r['ticker'] for r in csv.DictReader(open(fp))}
    tickers=sorted(tickers)
    data=fetch(tickers)
    with open('data/marketcap.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['ticker','marketCap','tier','shares','name'])
        for t in tickers:
            d=data.get(t,{})
            w.writerow([t,d.get('marketCap',''),tier(d.get('marketCap')),d.get('shares',''),d.get('name','')])
    from collections import Counter
    got=sum(1 for t in tickers if data.get(t,{}).get('marketCap'))
    print(f'market cap: {got}/{len(tickers)} tickers')
    print('tier dist:',dict(Counter(tier(data.get(t,{}).get('marketCap')) for t in tickers)))
