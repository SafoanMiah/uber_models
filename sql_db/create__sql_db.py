import os
import sqlite3

def create_database():

    #current dir
    current_dir = os.path.dirname(__file__)
    
    #connect to sqlite
    conn = sqlite3.connect(os.path.join(current_dir, 'database.db'))
    cursor = conn.cursor()
    
    #create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS database (
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

if __name__ == '__main__':
    create_database()