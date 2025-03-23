from typing import Union
import psycopg2
import os
from dotenv import load_dotenv
from psycopg2._psycopg import connection

load_dotenv()

def get_connection_to_postgres() -> connection:
    return psycopg2.connect(database= os.getenv("DATABASE"), user = os.getenv("USER"), password = os.getenv("PASSWORD"), host = "localhost", port = os.getenv("PORT"))




if __name__ == "__main__":
    conn = get_connection_to_postgres()
    print(type(conn))
    cursor = conn.cursor()
    query = """select version()"""
    cursor.execute(query)
    record = cursor.fetchall()
    print(f"DATABASE VERSION: {record}")
