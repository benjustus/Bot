"""Parser fuer Ken-French-CSV-Dateien und lokale Marktdaten."""
import re
import pandas as pd
import numpy as np

DATA = "/home/user/Bot/research/data"


def read_french(path, date_len=6, table_index=0):
    """Liest die n-te Tabelle (Standard: erste = Value-Weighted Monthly) einer
    Ken-French-CSV. Tabellen sind Bloecke von Zeilen, die mit YYYYMM (bzw.
    YYYYMMDD) beginnen; die Kopfzeile steht direkt davor."""
    with open(path, encoding="latin-1") as f:
        lines = f.readlines()
    pat = re.compile(r"^\s*(\d{%d})\s*," % date_len)
    tables, block, header = [], [], None
    for i, ln in enumerate(lines):
        if pat.match(ln):
            if not block:
                header = lines[i - 1].rstrip("\n")
            block.append(ln.rstrip("\n"))
        else:
            if block:
                tables.append((header, block))
                block = []
    if block:
        tables.append((header, block))
    header, block = tables[table_index]
    cols = [c.strip() for c in header.split(",")]
    cols[0] = "date"
    rows = [ln.split(",") for ln in block]
    df = pd.DataFrame(rows, columns=cols)
    df = df.apply(lambda s: pd.to_numeric(s, errors="coerce"))
    df["date"] = df["date"].astype(int)
    if date_len == 6:
        df.index = pd.PeriodIndex(df["date"].astype(str), freq="M")
    else:
        df.index = pd.to_datetime(df["date"].astype(str), format="%Y%m%d")
    df = df.drop(columns="date")
    df = df.replace([-99.99, -999.0], np.nan)
    return df


def factors_monthly():
    return read_french(f"{DATA}/F-F_Research_Data_Factors.csv")


def factors5_monthly():
    return read_french(f"{DATA}/F-F_Research_Data_5_Factors_2x3.csv")


def factors_daily():
    return read_french(f"{DATA}/F-F_Research_Data_Factors_daily.csv", date_len=8)


def mom_monthly():
    return read_french(f"{DATA}/F-F_Momentum_Factor.csv")


def strev_monthly():
    return read_french(f"{DATA}/F-F_ST_Reversal_Factor.csv")


def ltrev_monthly():
    return read_french(f"{DATA}/F-F_LT_Reversal_Factor.csv")


def portfolios(name):
    return read_french(f"{DATA}/Portfolios_Formed_on_{name}.csv")


def prior_portfolios(name="12_2"):
    return read_french(f"{DATA}/10_Portfolios_Prior_{name}.csv")


def spy_daily():
    df = pd.read_csv(f"{DATA}/spy_daily.csv", parse_dates=["date"], index_col="date")
    return df


def vix_daily():
    v = pd.read_csv(f"{DATA}/fred_vix.csv", parse_dates=["observation_date"],
                    index_col="observation_date")
    v.columns = ["vix"]
    v["vix"] = pd.to_numeric(v["vix"], errors="coerce")
    return v.dropna()
