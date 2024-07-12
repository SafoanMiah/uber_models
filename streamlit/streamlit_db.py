import streamlit as st
import sqlite3
import pandas as pd

#copy as i cannot figure out why reading files outside of dir gives error in streamlit

def create():
    conn = sqlite3.connect('streamlit_rides.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS streamlit_rides (
            price STRING,
            distance STRING,
            pickup STRING,
            dropoff STRING,
            time STRING
        )
    ''')

    conn.commit()
    conn.close()

def insert(price, distance, pickup, dropoff, time):
    conn = sqlite3.connect('streamlit_rides.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO streamlit_rides (price, distance, pickup, dropoff, time)
        VALUES (?, ?, ?, ?, ?)
    ''', (price, distance, pickup, dropoff, time))

    conn.commit()
    conn.close()

def read():
    conn = sqlite3.connect('streamlit_rides.db')
    
    query = "SELECT * FROM streamlit_rides;"
    
    df = pd.read_sql_query(query, conn)
    
    conn.close()
    
    return df


def clear():
    conn = sqlite3.connect('streamlit_rides.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM streamlit_rides')

    conn.commit()
    conn.close()