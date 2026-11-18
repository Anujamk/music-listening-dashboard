# Music Listening Dashboard

An end-to-end data project: a listening-history CSV is cleaned with pandas, loaded into PostgreSQL, served through FastAPI endpoints, and visualized with Chart.js.

**Status:** Work in progress. Data cleaning is done; the database schema is next.

## Stack
Python 3.11+, pandas, PostgreSQL, psycopg 3 (raw SQL, no ORM), Pydantic, FastAPI, Chart.js

## Setup

1. **Clone the repo and create a virtual environment**
   ```
   git clone https://github.com/Anujamk/music-dashboard.git
   cd music-dashboard
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # Mac/Linux
   pip install -r requirements.txt
   ```

2. **Create the database**
   In psql or pgAdmin: `CREATE DATABASE music;`

3. **Configure environment variables**
   Copy `.env.example` to `.env` and fill in your Postgres password.

4. **Get the data**
   Download the [Spotify Streaming History](https://mavenanalytics.io/data-playground) dataset from Maven Analytics and save it as `data/spotify_history.csv`.

5. **Run the pipeline** (from the project root)
   ```
   python scripts/check_db.py    # verify the database connection
   python scripts/clean.py       # clean the raw CSV -> data/plays_clean.csv
   ```

## Project structure
```
data/        raw and cleaned CSVs (not committed)
scripts/     one-off scripts: DB check, cleaning, ingestion
notebooks/   data exploration
app/         FastAPI application (coming)
static/      dashboard page (coming)
```

## Design decisions
See [DECISIONS.md](DECISIONS.md) for every design choice and the reasoning behind it.