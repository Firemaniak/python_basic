#-------------------------------------------Task_#1---------------------------------------------------------------------
#---------------------------------------Список всех стран---------------------------------------------------------------
# Используя базу данных world, выведи названия всех стран из таблицы country.
# Каждое название должно отображаться с новой строки и иметь номер.

#pip install pymysql
# import pymysql
#
# with pymysql.connect(
#     host='ich-db.edu.itcareerhub.de',
#     user='ich1',
#     password='password',
#     database='world'
# ) as connection:  # автоматически закроет connection
#
#
#     with connection.cursor() as cursor:  # автоматически закроет cursor
#
#         cursor.execute("SELECT name FROM country")
#
#     for i, row in enumerate(cursor.fetchall(), start=1):
#         print(f'{i}. {row[0]}')

#------------------------------------------------Task_#2----------------------------------------------------------------
#----------------------------------------Города выбранной страны--------------------------------------------------------
# Добавьте к предыдущей программе возможность выбора страны. Пользователь введёт название или номер из выведенного списка.
# Далее выведите все города этой страны и их численность населения, также с нумерацией.

import pymysql

with pymysql.connect(
    host='ich-db.edu.itcareerhub.de',
    user='ich1',
    password='password',
    database='world'
) as connection:  # автоматически закроет connection


    with connection.cursor() as cursor:  # автоматически закроет cursor

        cursor.execute("SELECT name FROM country")
        countries = cursor.fetchall()

        for i, row in enumerate(countries, start=1):
            print(f'{i}. {row[0]}')

        selected = input("Enter a country name or number: ")

        if selected.isdigit():
            country_name = countries[int(selected) - 1][0]
        else:
            country_name = selected

        cursor.execute(
        """
            SELECT city.Name, city.Population
            FROM city
            JOIN country ON country.Code = city.CountryCode
            WHERE country.Name = %s
            ORDER BY city.Population DESC
            """,
            (country_name.lower(),)
        )

        cities = cursor.fetchall()

        print(f'\nВыберите страну: {country_name}')

        for i, row in enumerate(cities, start=1):
            city = row[0]
            population = row[1]
            print(f'{i}. {city} - {population}')

#-----------------------------------------------------------------------------------------------------------------------