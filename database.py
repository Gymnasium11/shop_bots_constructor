import sqlite3


def read(request):
    """на вход функции необходимо передать запрос на вставку"""
    try:
        sqlite_connection= sqlite3.connect('base.db', timeout=20)
        cursor = sqlite_connection.cursor()
        # print("Подключен к SQLite")

        sqlite_select_query = request
        cursor.execute(sqlite_select_query)
        total_rows = cursor.fetchall()
        # print("Всего строк:  ", total_rows)
        cursor.close()
        return total_rows

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")


def insert(reaquest):
    """на вход функции необходимо передать запрос на вставку"""
    try:
        sqlite_connection = sqlite3.connect('base.db')
        cursor = sqlite_connection.cursor()
        # print("База данных подключена к SQLite")

        sqlite_insert_query = reaquest

        count = cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        # print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Не удалось вставить данные в таблицу sqlite")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        # exc_type, exc_value, exc_tb = sys.exc_info()
        # print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


if __name__ == "__main__":
    # insert("""INSERT INTO shop
    #                           (name, token, admins, rating, count_solled, discreption)  VALUES  ("third", "this_is_token_1111", "admin3", 4.1, 1520, "third shop for test")""")
    print(read("SELECT * FROM shop"))
