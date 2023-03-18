
# Sparkify Data Pipline & Database

## Project Description/Purpose

Sparkify, a music streaming startup, has been collecting data about songs and user activity in JSON files. The company aims to analyze this data to understand user behavior, preferences, and trends to make data-driven decisions and improve their service.

To make the data easily accessible and useful for analysis, it is necessary to create a structured database that organizes the data in a meaningful way. This database will help Sparkify's analytics team perform queries and gain insights that can drive the company's strategic and operational decisions.

## Database Schema Design

The database uses a star schema with a central fact table songplays and four dimension tables: users, songs, artists, and time. The star schema is an excellent choice for this scenario because it provides fast aggregations and simplifies queries for analytical purposes.

### Fact Table

1. songplays: Records in log data associated with song plays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)

### Dimension Tables

2. users: Users in the app (user_id, first_name, last_name, gender, level)

3. songs: Songs in the music database (song_id, title, artist_id, year, duration)

4. artists: Artists in the music database (artist_id, name, location, latitude, longitude)

5. time: Timestamps of records in songplays broken down into specific units (start_time, hour, day, week, month, year, weekday)


## ETL Pipeline

The ETL pipeline consists of three main steps:

1. Extract: Read JSON data from `song_data` and `log_data` files.

2. Transform: Process the data to fit the schema structure and convert relevent fields (e.g., converting timestamp to datetime).

3. Load: Instert the transformed data into the corresponding tables in the database. 

The ETL script `etl.py` contains functions to process song files and log files separately, and a main function to run the ETL process for all files in the specified directories. 

## Exampley Queries for Song Play Analysis

1. Find the top 10 most popular songs by play count:
```

```

2. Find the number of active users by subscription level (free or paid):
```

```


3. Find the top 5 busiest hours for song plays:
```

```

