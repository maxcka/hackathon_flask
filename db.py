
from psycopg_pool import ConnectionPool
from dotenv import dotenv_values

conn_string = "host='35.197.53.40' dbname='postgres' user='hwap10' password='#trr@Pk1~[sxme68'"

pool = ConnectionPool(
    conn_string
)
# the pool starts connecting immediately.


def query(query: str, args: list = []):
    with pool.connection() as conn:
        return conn.execute(query, args).fetchall()
    



# def addEvent(name, ...):
#     ..
#     query('INSERT INTO team10.events" ....')