from django.db import connection
from contextlib import closing


def get_quest_info(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""update univer_quest set "quest" = "quest" + 1 where id = %s returning * """, [pk])
        quest = dict_fetchone(cursor)
    return quest


def get_menu():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from univer_menu""")
        menu = dict_fetchall(cursor)
    return menu


def get_teachers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from univer_teacher""")
        teach = dict_fetchall(cursor)
    return teach


def get_basic():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from univer_basic_menu""")
        basic = dict_fetchall(cursor)
    return basic


def get_news():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from univer_news""")
        news = dict_fetchall(cursor)
    return news


def get_category():
    with closing(connection.cursor()) as cur:
        cur.execute("""select * from univer_category""")
        categories = dict_fetchall(cur)
    return categories


def get_news_by_id(pk):
    with closing(connection.cursor()) as cur:
        cur.execute("""select * from univer_news where category_id = %s """, [pk])
        news_id = dict_fetchall(cur)
    return news_id


def get_basic_by_id(pk):
    with closing(connection.cursor()) as cur:
        cur.execute("""select * from univer_news where basic_id = %s """, [pk])
        news_id = dict_fetchall(cur)
    return news_id


def get_news_by_id_one(pk):
    with closing(connection.cursor()) as cur:
        cur.execute("""update univer_news set "views" = "views" + 1 where id = %s returning *""", [pk])
        news_one = dict_fetchone(cur)
    return news_one


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row))
            for row in cursor.fetchall()]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
