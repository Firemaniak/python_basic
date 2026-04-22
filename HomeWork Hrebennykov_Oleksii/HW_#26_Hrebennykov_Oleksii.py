# -----------------------------------------------Список файлов и папок--------------------------------------------------
# Напишите программу, которая принимает путь к директории через аргумент командной строки и выводит:
# Отдельно список папок
# Отдельно список файлов
#
# Пример запуска
# python script.py /home/user/documents
#
# Пример вывода
# Содержимое директории '/home/user/documents':
#
# Папки:
# - folder1
# - folder2
#
# Файлы:
# - file1.txt
# - file2.txt
# - notes.docx

import os
import sys

# берём путь из аргументов
path = sys.argv[1]

folders = []
files = []

for item in os.listdir(path):
    full_path = os.path.join(path, item)

    if os.path.isdir(full_path):
        folders.append(item)
    elif os.path.isfile(full_path):
        files.append(item)

print(f"Содержимое директории '{path}':\n")

print("Папки:")
for folder in folders:
    print(f"- {folder}")

print("\nФайлы:")
for file in files:
    print(f"- {file}")