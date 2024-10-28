from flask import Flask, jsonify, request
from flask_cors import CORS 
import sqlite3
import random

app = Flask(__name__)
CORS(app)  # To allow cross-origin requests (needed for frontend-backend interaction)

DATABASE = 'database.db'

# Initialize database with sample air quality data
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS air_quality (
                        id INTEGER PRIMARY KEY,
                        location TEXT NOT NULL,
                        lat REAL NOT NULL,
                        lon REAL NOT NULL,
                        pm25 REAL NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                      )''')
    conn.commit()
    conn.close()

# Insert sample data
def insert_sample_data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    sample_locations = [
        {"location": "Location A", "lat": 37.7749, "lon": -122.4194, "pm25": random.uniform(10, 50)},
        {"location": "Location B", "lat": 34.0522, "lon": -118.2437, "pm25": random.uniform(10, 50)}
    ]
    for loc in sample_locations:
        cursor.execute("INSERT INTO air_quality (location, lat, lon, pm25) VALUES (?, ?, ?, ?)",
                       (loc["location"], loc["lat"], loc["lon"], loc["pm25"]))
    conn.commit()
    conn.close()

# Route to get air quality data
@app.route('/api/air_quality', methods=['GET'])
def get_air_quality_data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT location, lat, lon, pm25, timestamp FROM air_quality")
    rows = cursor.fetchall()
    conn.close()
    data = [{"location": row[0], "lat": row[1], "lon": row[2], "pm25": row[3], "timestamp": row[4]} for row in rows]
    return jsonify(data)

if __name__ == '__main__':
    init_db()   # Initialize database
    insert_sample_data()  # Insert sample data on first run
    app.run(debug=True)
