import os
import psycopg
from flask import g
from dotenv import load_dotenv

load_dotenv()

from helpers.application import app

def get_connection():
    conn = getattr(g, '_database', None)
    if conn is None:
        # se der error coloque o nome dos dados que precisa
        # depois do nome da variavel de ambiente.
        conn = g._database = psycopg.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
    return conn


@app.teardown_appcontext
def close_connection(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()