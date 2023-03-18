# 1. Find the top 10 most popular songs by play count:
top_10_songs = ("""
    SELECT s.title, a.name, COUNT(*) as play_count
    FROM songplays sp
    JOIN songs s ON sp.song_id = s.song_id
    JOIN artists a ON sp.artists_id = a.artists_id
    GROUP BY s.title, a.name
    ORDER BY play_count DESC
    LIMIT 10;
""")

# 2. Find the number of active users by subscription level (free or paid):
active_users = ("""
    SELECT level, COUNT(DISTINCT user_id) as user_count
    FROM songplays
    GROUP BY level;
""")

# 3. Find the top 5 busiest hours for song plays:
busy_hours = ("""
    SELECT t.hour, COUNT(*) as play_count
    FROM songplays sp
    JOIN time t ON sp.start_time = t.start_time
    GROUP BY t.hour
    ORDER BY play_count DESC
    LIMIT 5;
""")