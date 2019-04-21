import sqlite3

conn = sqlite3.connect("cartoon.db", check_same_thread=False)

c = conn.cursor()


def insert_content(category_id, episode, content):
    c.execute(
        "insert into subtitle(category_id,episode,content) values ({category_id},{episode},{content})".format(
            category_id=category_id, episode=episode, content=content))
    conn.commit()


def get_category(id):
    result = c.execute("select * from category where id ={id}".format(id=id))
    return result.fetchone()


def get_subtitle(category_id, episode):
    data = c.execute(
        "select * from subtitle where category_id={category_id} and episode={episode}".format(category_id=category_id,
                                                                                              episode=episode))
    return data.fetchone()
