import psycopg2
import logging
from utils.utils import get_connection_to_postgres


def create_tables():

    commands = (
        """
        CREATE TABLE IF NOT EXISTS public.JUMPER  (
        JUMPER_ID INTEGER PRIMARY KEY,
        FIRST_NAME VARCHAR(255) NOT NULL,
        LAST_NAME VARCHAR(255) NOT NULL,
        BIRTH_DATE DATE NOT NULL,
        IS_ACTIVE BOOLEAN NOT NULL,
        COUNTRY VARCHAR(50) NOT NULL,
        CLUB VARCHAR(50) NOT NULL)
        """,
    )

    try:
        conn = get_connection_to_postgres()
        with conn.cursor() as cursor:
            for command in commands:
                cursor.execute(command)
                conn.commit()
                logging.info("Tables created succesfully")
    except (psycopg2.DatabaseError, Exception) as exception:
        logging.exception(exception)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_tables()