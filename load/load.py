import os
import psycopg
from dotenv import load_dotenv


def connect_to_db():
    """
    Connect to the PostgreSQL database using environment variables.
    Returns a connection object.
    """
    # Load environment variables
    load_dotenv()

    # Connect to PostgreSQL
    conn = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    print("Successfully connected to PostgreSQL!")
    return conn


def call_to_db(query, params=None):
    """
    Execute a query against the PostgreSQL database.
    Returns the result of the query.
    """
    conn = connect_to_db()
    with conn.cursor() as cur:
        cur.execute(query, params)
        result = cur.fetchall()
    conn.close()
    return result