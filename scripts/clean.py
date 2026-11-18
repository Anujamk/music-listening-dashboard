from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = PROJECT_ROOT / "data" / "spotify_history.csv"
CLEAN_PATH = PROJECT_ROOT / "data" / "plays_clean.csv"
KEEP_COLUMNS = ["spotify_track_uri", "ts", "ms_played", "track_name", "artist_name", "album_name"]

def load_csv(path):
    """loads the csv from the path into a dataframe"""
    df = pd.read_csv(path)
    return df


def parse_timestamps(df):
    """converts ts to UTC datetime, counts and reports rows that failed to parse"""
    df["ts"] = pd.to_datetime(df["ts"], errors="coerce", utc=True)
    NaT_count = df["ts"].isna().sum()
    df = df.dropna(subset="ts")
    print(f"Dropped {NaT_count} null timestamps")
    return df


def keep_columns(df):
    """keeps columns: spotify_track_uri, ts, ms_played, track_name, artist_name, album_name"""
    df = df[KEEP_COLUMNS]
    return df


def drop_duplicate_rows(df):
    """drop duplicate rows except the first and prints the count"""
    len_before = len(df)
    df = df.drop_duplicates()
    len_after = len(df)
    n = len_before - len_after
    print(f"Dropped {n} duplicate rows")
    return df


def add_is_real_play(df):
    """add column is_real_play, true if ms_played >= 30000"""
    df["is_real_play"] = df["ms_played"] >= 30000
    return df


def save_csv(df, path):
    """save the clean csv in path"""
    df.to_csv(path, index=False)
    return


def main():
    df = load_csv(RAW_PATH)
    df = drop_duplicate_rows(df)
    df = keep_columns(df)
    df = parse_timestamps(df)
    df = add_is_real_play(df)
    save_csv(df, CLEAN_PATH)


if __name__ == "__main__":
    main()