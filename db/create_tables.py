import psycopg2
import logging
from utils.utils import get_connection_to_postgres


def create_tables() -> None:

    commands = (
        """
        CREATE TABLE IF NOT EXISTS public.JUMPER (
        JUMPER_ID INTEGER PRIMARY KEY,
        FIRST_NAME VARCHAR(255) NOT NULL,
        LAST_NAME VARCHAR(255) NOT NULL,
        BIRTH_DATE DATE NOT NULL,
        IS_ACTIVE BOOLEAN NOT NULL,
        COUNTRY VARCHAR(50) NOT NULL,
        CLUB VARCHAR(50) NOT NULL)
        """,
        """
        CREATE TABLE IF NOT EXISTS public.HILL (
        HILL_ID INTEGER PRIMARY KEY,
        HILL_NAME VARCHAR(255) NOT NULL,
        CITY VARCHAR(255) NOT NULL,
        K_POINT INTEGER NOT NULL,
        HILL_SIZE INTEGER NOT NULL,
        HILL_RECORD_ID INTEGER NOT NULL
        )""",
        """
        CREATE TABLE IF NOT EXISTS public.EVENT (
        EVENT_ID INTEGER PRIMARY KEY,
        HILL_ID INTEGER NOT NULL,
        WINNER_ID INTEGER NOT NULL,
        CONSTRAINT fk_hill_id FOREIGN KEY(HILL_ID) REFERENCES public.HILL(HILL_ID),
        CONSTRAINT fk_winner_id FOREIGN KEY(WINNER_ID) REFERENCES public.jumper(JUMPER_ID))""",
        """
        CREATE TABLE IF NOT EXISTS public.JUMP (
        JUMP_ID INTEGER PRIMARY KEY,
        JUMPER_ID INTEGER NOT NULL,
        EVENT_ID INTEGER NOT NULL,
        DISTANCE NUMERIC NOT NULL,
        STYLE_POINTS NUMERIC NOT NULL,
        WIND_POINTS NUMERIC,
        GATE_POINTS NUMERIC,
        TOTAL_POINTS NUMERIC NOT NULL,
        ROUND VARCHAR(30) NOT NULL,
        DISQUALIFIED BOOLEAN NOT NULL,
        HILL_ID INTEGER NOT NULL,
        CONSTRAINT fk_jumper_id FOREIGN KEY(JUMPER_ID) REFERENCES public.JUMPER(JUMPER_ID),
        CONSTRAINT fk_event_id FOREIGN KEY(EVENT_ID) REFERENCES public.EVENT(EVENT_ID),
        CONSTRAINT fk_hill_id FOREIGN KEY(HILL_ID) REFERENCES public.HILL(HILL_ID))
        """
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