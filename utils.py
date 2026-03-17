import streamlit as st
import psycopg2
import pandas as pd

@st.cache_resource(show_spinner="Connecting to PostgreSQL...")
def get_connection():
    try:
        return psycopg2.connect(
            host="localhost",
            database="hospital_db",
            user="postgres",
            password="123",
            port="5433"
        )
    except Exception as e:
        st.error(f"Cannot connect to database: {e}")
        st.stop()

def run_query(query):
    conn = get_connection()
    return pd.read_sql(query, conn)