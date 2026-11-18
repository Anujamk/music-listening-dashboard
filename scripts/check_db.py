from dotenv import load_dotenv
import os
import psycopg

load_dotenv()

db_url = os.environ["DATABASE_URL"]
with psycopg.connect(db_url) as conn:
    with conn.cursor() as cur:
        cur.execute("""SELECT 1""")
        check = cur.fetchone()
        print(check[0])
