import sqlite3

try:
    sqlite_connection = sqlite3.connect('database.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    email text NOT NULL UNIQUE,
                                    joining_date datetime,
                                    salary REAL NOT NULL);'''
    cursor.execute(sqlite_create_table_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")


# conn = sqlite3.connect("mydatabase.db")
# # conn.row_factory = sqlite3.Row
# cursor = conn.cursor()
#
# sql = "SELECT * FROM albums WHERE artist=?"
# cursor.execute(sql, [("Red")])
# print(cursor.fetchall())  # or use fetchone()
#
# print("Here's a listing of all the records in the table:")
# for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
#     print(row)
#
# print("Results from a LIKE query:")
# sql = "SELECT * FROM albums WHERE title LIKE 'The%'"
# cursor.execute(sql)
#
# print(cursor.fetchall())