
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

![image](https://user-images.githubusercontent.com/111329424/226097824-06fb085f-34a1-48ed-a244-006018bb38fd.png)

## ETL Pipeline

The ETL pipeline consists of three main steps:

1. Extract: Read JSON data from `song_data` and `log_data` files.

2. Transform: Process the data to fit the schema structure and convert relevent fields (e.g., converting timestamp to datetime).

3. Load: Instert the transformed data into the corresponding tables in the database. 

The ETL script `etl.py` contains functions to process song files and log files separately, and a main function to run the ETL process for all files in the specified directories. 

## Exampley Queries for Song Play Analysis

1. Find the total play count for each gender, also showing how many of each gender for further analysis:
```
SELECT gender_stats.gender, play_count, user_count 
FROM (SELECT u.gender, COUNT(*) as play_count 
      FROM songplays sp JOIN users u ON sp.user_id = u.user_id 
      GROUP BY u.gender) as gender_stats 
JOIN (SELECT gender, COUNT(*) as user_count 
      FROM users 
      GROUP BY gender) as user_stats ON gender_stats.gender = user_stats.gender 
ORDER BY play_count DESC;
```
>>> * postgresql://student:***@127.0.0.1/sparkifydb
2 rows affected.
>>>

| gender |  play_count |  user_count |
| :---     |    ---: |    ---: |
| F   |  4887    |  55    |
| M     |  1933     |  41     |


2. Find the number of active users by subscription level (free or paid):
```
SELECT level, COUNT(DISTINCT user_id) as user_count
FROM songplays
GROUP BY level;
```
>>> * postgresql://student:***@127.0.0.1/sparkifydb
>>> 2 rows affected.

| level |  user_count |
| :---     |    ---: |
| free   |  82    |
| paid     |  22     |


3. Find the top 5 busiest hours for song plays:
```
SELECT t.hour, COUNT(*) as play_count
FROM songplays sp
JOIN time t ON sp.start_time = t.start_time
GROUP BY t.hour
ORDER BY play_count DESC
LIMIT 5;
```
>>> * postgresql://student:***@127.0.0.1/sparkifydb
>>> 5 rows affected.

| hour |  play_count |
| :---     |    ---: |
| 16   |  542    |
| 18     |  498     |
| 17   |  494    |
| 15     |  477     |
| 14   |  432    |
