import sqlite3

conn = sqlite3.connect("cartoon.db", check_same_thread=False)

c = conn.cursor()


def create_table():
    c.execute(
        "create table cartoon (sid INTEGER PRIMARY KEY,description message_text ,subtitiles message_text ) ")
    conn.commit()
    conn.close()


def db_close():
    conn.close()


def get_cartoon(sid):
    data = c.execute("select * from cartoon where sid='{sid}'".format(sid=sid))
    return data.fetchone()
