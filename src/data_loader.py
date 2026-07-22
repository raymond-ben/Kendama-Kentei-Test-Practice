from pathlib import Path
import pandas as pd

DATA_FILE = Path("data/tricks.xlsx")

def load_tricks():
    df = pd.read_excel(DATA_FILE)

    df.columns = [
        "level",
        "class",
        "number",
        "trick"
    ]

    df = df.dropna()

    df["level"] = df["level"].astype(str).str.strip()
    df["class"] = df["class"].astype(str).str.strip()
    df["trick"] = df["trick"].astype(str).str.strip()

    df["number"] = df["number"].astype(int)

    return df

def get_levels():
    df = load_tricks()
    return df["level"].unique().tolist()

def get_classes(level):
    df = load_tricks()
    return df[df["level"] == level]["class"].unique().tolist()

def get_tricks(level, kclass):
    df = load_tricks()

    filtered = df[
        (df["level"] == level) &
        (df["class"] == kclass)
    ]

    return filtered.sort_values("number")["trick"].tolist()