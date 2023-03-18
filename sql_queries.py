# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY, 
    start_time TIMESTAMP NOT NULL, 
    user_id INT NOT NULL, 
    level VARCHAR(255), 
    song_id VARCHAR(255), 
    artist_id VARCHAR(255), 
    session_id INT NOT NULL, 
    location VARCHAR(255), 
    user_agent VARCHAR(255));
""")

user_table_create = (""" CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY, 
    first_name VARCHAR(255), 
    last_name VARCHAR(255), 
    gender CHAR(5), 
    level VARCHAR(255) NOT NULL);
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR(255) PRIMARY KEY, 
    title VARCHAR(255) NOT NULL, 
    artist_id VARCHAR(255) NOT NULL, 
    year INT NOT NULL, 
    duration NUMERIC NOT NULL);
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR(255) PRIMARY KEY, 
    name VARCHAR(255) NOT NULL, 
    location VARCHAR(255), 
    latitude DOUBLE PRECISION, 
    longitude DOUBLE PRECISION);
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY, 
    hour INT NOT NULL, 
    day INT NOT NULL, 
    week INT NOT NULL, 
    month INT NOT NULL, 
    year INT NOT NULL, 
    weekday INT NOT NULL);
""")

# INSERT RECORDS

songplay_table_insert = (""" 
    INSERT INTO songplays (
    start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = (""" 
    INSERT INTO users (
    user_id, first_name, last_name, gender, level) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (user_id) 
    DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = (""" 
    INSERT INTO songs (
    song_id, title, artist_id, year, duration) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (song_id) 
    DO NOTHING;
""")

artist_table_insert = (""" 
    INSERT INTO artists (
    artist_id, name, location, latitude, longitude) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (artist_id) 
    DO NOTHING;
""")

time_table_insert = (""" 
    INSERT INTO time (
    start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) 
    DO NOTHING;
""")

# FIND SONGS

song_select = (""" 
    SELECT songs.song_id, songs.artist_id
    FROM songs
    JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.duration = %s;
""")


# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, time_table_create, song_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, artist_table_drop, time_table_drop, song_table_drop, songplay_table_drop]

# FOREIGN KEY (start_time) REFERENCES time (start_time),
#    FOREIGN KEY (user_id) REFERENCES users (user_id),
#    FOREIGN KEY (song_id) REFERENCES songs (song_id),
#    FOREIGN KEY (artist_id) REFERENCES artists (artist_id),
#    UNIQUE (start_time, user_id, song_id, artist_id)