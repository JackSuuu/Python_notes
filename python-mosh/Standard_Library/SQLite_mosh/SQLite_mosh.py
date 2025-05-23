import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("/Users/jack/Desktop/Python/Python_standard_library/Files_mosh/movies.json").read_text())
print(movies)

with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?, ?, ?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()

