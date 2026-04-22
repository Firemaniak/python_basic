# import os
# import sys
#
# # берём путь из аргументов
# path = sys.argv[1]
#
# folders = []
# files = []
#
# for item in os.listdir(path):
#     full_path = os.path.join(path, item)
#
#     if os.path.isdir(full_path):
#         folders.append(item)
#     elif os.path.isfile(full_path):
#         files.append(item)
#
# print(f"Содержимое директории '{path}':\n")
#
# print("Папки:")
# for folder in folders:
#     print(f"- {folder}")
#
# print("\nФайлы:")
# for file in files:
#     print(f"- {file}")

#-----------------------------Поиск и удаление файлов с указанным расширением-------------------------------------------
# Напишите программу, которая:
# Принимает путь к директории и расширение файлов через аргумент командной строки.
# Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
# Спрашивает у пользователя, хочет ли он удалить найденные файлы.
# Если пользователь подтверждает, удаляет их.
#
# Пример запуска:
# python script.py /home/user/PycharmProjects/project1 .log
# Пример вывода
#
# Найдены файлы с расширением '.log':
#
# - logs/error.log
# - logs/system.log
# - logs/backup/old.log
# - logs/backup/debug.log
#
#
# Вы хотите удалить эти файлы? (y/n): y
#
# Удаление завершено.

import os

path = "C:/Users/ICH/Desktop/HW_26_Python"
extension = ".log"

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(extension):
            print(os.path.join(root, file))

#----------------------------------------------------------------------------------------------------------------------







