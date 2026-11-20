DROP TABLE IF EXISTS plays;
DROP TABLE IF EXISTS tracks;
DROP TABLE IF EXISTS artists;


CREATE TABLE artists(
    artist_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    artist_name TEXT NOT NULL,
    UNIQUE (artist_name)
);

CREATE TABLE tracks(
    spotify_track_uri TEXT NOT NULL PRIMARY KEY,
    track_name TEXT NOT NULL,
    artist_id INTEGER NOT NULL REFERENCES artists (artist_id),
    album_name TEXT NOT NULL
);

CREATE TABLE plays(
    play_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    spotify_track_uri TEXT NOT NULL REFERENCES tracks (spotify_track_uri),
    ts TIMESTAMPTZ NOT NULL,
    ms_played INTEGER NOT NULL,
    is_real_play BOOLEAN NOT NULL,
    UNIQUE (spotify_track_uri, ts)
);

