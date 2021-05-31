from django.db import connection
from contextlib import closing


def get_menu():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from univer_menu""")
        menu = dict_fetchall(cursor)
    return menu

def get_news():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""delect * from univer_news""")





def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row))
            for row in cursor.fetchall()]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.descriprion]
    return dict(zip(columns, row))
