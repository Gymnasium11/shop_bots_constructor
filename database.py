import sqlite3


def read_sqlite_table():
    try:
        sqlite_connection= sqlite3.connect('base.db', timeout=20)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT count(*) from sqlitedb_developers"""
        cursor.execute(sqlite_select_query)
        total_rows = cursor.fetchone()
        print("Всего строк:  ", total_rows)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

read_sqlite_table()

