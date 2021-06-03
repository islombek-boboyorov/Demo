from django.db import connection
from contextlib import closing


def get_menu():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from univer_menu""")
        menu = dict_fetchall(cursor)
    return menu


def get_basic():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from univer_basic_menu """)
        menu_id = dict_fetchall(cursor)
    return menu_id


def get_category():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from univer_category""")
        cat = dict_fetchall(cursor)
    return cat


def get_teacher():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from univer_teacher""")
        teacher = dict_fetchall(cursor)
    return teacher


def get_news():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from univer_news""")
        news = dict_fetchall(cursor)
    return news


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