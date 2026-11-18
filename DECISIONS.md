# Design Decisions

## Setup
1. **DB credentials live in `.env`, never in code.** Keeps secrets out of Git, and lets the same code run on different machines (laptop, Docker, server) with different credentials.
2. **One `DATABASE_URL` instead of separate host/user/password variables.** One value to change when switching databases, and most hosted Postgres providers give you a URL anyway.
3. **`os.environ[...]`, not `os.getenv(...)`, for required config.** Fails fast with a clear `KeyError` instead of returning `None` and causing a confusing error later.
4. **Notebooks for exploration only; pipeline code lives in `.py` scripts.** Scripts can be run from the command line, tested, and produce clean Git diffs.
5. **`requirements.txt` holds app dependencies only; dev tools (ipykernel) are kept out.** The app shouldn't install tools it doesn't need to run.

## Data
6. **Using the Maven Analytics Spotify dataset (~150k plays) while my Apple Music export is pending.** Unblocks Phase 1 now; the pipeline will be adapted to my own data later.
7. **The raw CSV in `data/` is never modified; cleaning writes a new file.** Anything dropped can always be recovered from the source.

## Cleaning
8. **Parse `ts` to datetime with `errors='coerce'` and count any failures.** Every planned chart depends on time; bad values become `NaT` and get counted, not silently ignored.
9. **Store timestamps in UTC; convert to the user's timezone in the API.** Single source of truth in the DB; any timezone can be shown at query time.
10. **Drop exact duplicate rows (keep first) and log the count.** The same track starting at the same second, with identical fields, can't be two real plays; it's an export/logging artifact.
11. **Flag plays under 30s with `is_real_play` instead of deleting them.** 30s matches the industry standard Spotify uses to count a stream; flagging keeps the raw data and lets the threshold change without re-cleaning.
12. **Drop the `skipped` column.** It's unreliable (e.g. 0 ms plays marked `skipped=False`); `is_real_play` replaces it.
13. **Drop `reason_start`, `reason_end`, `shuffle`, `platform`.** Not used by any planned feature; cleaning unused columns is wasted effort.
14. **Keep `spotify_track_uri`.** It uniquely identifies a track; names don't (different artists can share a song title, and the same song appears on multiple albums).

**Final cleaned columns:** `spotify_track_uri`, `ts`, `ms_played`, `track_name`, `artist_name`, `album_name`, `is_real_play`
15. **Commit the exploration notebook (outputs cleared).** It shows the evidence behind the cleaning decisions.