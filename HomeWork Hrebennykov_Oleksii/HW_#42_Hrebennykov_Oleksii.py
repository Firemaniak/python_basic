#-------------------------------------------------Task_#1---------------------------------------------------------------
#----------------------------------------------Создание базы------------------------------------------------------------
# Напишите программу, которая:
# создаёт базу данных notes_app_<your_group>_<your_full_name>
# выбирает эту базу через USE notes_app
# выводит сообщение о результате

# import pymysql
# from pymysql.cursors import DictCursor
#
# config = {
#     'host': 'ich-edit.edu.itcareerhub.de',
#     'user': 'ich1',
#     'password': 'ich1_password_ilovedbs',
# }
#
# database_name = "notes_app_121225_ptm_Hrebennykov"
#
# try:
#     with pymysql.connect(**config, cursorclass=DictCursor) as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
#             cursor.execute(f"USE {database_name}")
#
#
#             print(f"Database {database_name} created or already exists.")
#
# except Exception as error:
#
#     print(f"Database error: {error}")

#------------------------------------------------Task_#2----------------------------------------------------------------
#-------------------------------------------Добавление заметок----------------------------------------------------------

# Продолжите предыдущую программу:
# создайте таблицу notes с полями: id, title, content
# вставьте одну заметку в таблицу
# выполните commit() после вставки
# выведите все заметки используя DictCursor

import pymysql
from pymysql.cursors import DictCursor


config = {
    'host': 'ich-edit.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'ich1_password_ilovedbs',
}

database_name = "notes_app_121225_ptm_Hrebennykov"


try:

    with pymysql.connect(
        **config,
        cursorclass=DictCursor
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS {database_name}"
            )

            cursor.execute(f"USE {database_name}")

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS notes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255),
                    content TEXT
                )
                """
            )

            title = "Shopping list"
            content = "Milk, bread, eggs"

            cursor.execute(
                """
                INSERT INTO notes (title, content)
                VALUES (%s, %s)
                """,
                (title, content)
            )

            connection.commit()

            print(f"Note added: {title}")

except Exception as error:

    print(f"Database error: {error}")

#-----------------------------------------------------------------------------------------------------------------------
