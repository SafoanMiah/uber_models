import sqlite3

def create_database():
    
    #connect to sqlite
    conn = sqlite3.connect('uber_cost_prediction/sql_db/uber_rides.db')
    cursor = conn.cursor()
    
    #create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uber_rides (
            fare_amount REAL,
            distance_km REAL,
            pickup_longitude REAL,
            pickup_latitude REAL,
            dropoff_longitude REAL,
            dropoff_latitude REAL,
            passenger_count INTEGER,
            year INTEGER,
            month INTEGER,
            day INTEGER,
            hour INTEGER
        )
    ''')

    conn.commit()
    conn.close()

create_database()