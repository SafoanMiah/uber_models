import sqlite3
import pandas as pd

df = pd.read_csv('data/processed_data.csv')

conn = sqlite3.connect('sql_db/uber_rides.db')

# Insert data into the database
df.to_sql('uber_rides', conn, if_exists='append', index=False)
conn.close()