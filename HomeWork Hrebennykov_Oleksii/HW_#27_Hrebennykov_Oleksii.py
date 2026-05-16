#--------------------------------------------------#Task_#1-------------------------------------------------------------
# Фильтрация по ключевому слову
#
# Напишите программу, которая ищет в файле все строки, содержащие указанное пользователем слово, и сохраняет их в новый файл.
# Имя нового файла формируется как <keyword>_<original_filename>.
# Если файл не существует, программа должна вывести ошибку.
# Если совпадения не найдены, новый файл не создаётся.
# Используйте файл system_log.txt.
#
# Пример ввода:
# Введите имя файла для поиска: system_log.txt
# Введите ключевое слово: error
#
# Пример вывода:
# Строки, содержащие 'error', сохранены в error_system_log.txt.

file_name = input("Введите имя файла для поиска: ")
key_word = input("Введите ключевое слово: ")

new_filename = f"{key_word}_{file_name}"

try:
    found_lines = []

    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            if key_word.lower() in line.lower():
                found_lines.append(line)

    if found_lines:
        with open(new_filename, "w", encoding="utf-8") as file:
            for line in found_lines:
                file.write(line)

        print(f"Строки содержащие {key_word}, сохранены в {new_filename}")
    else:
        print(f"Строки, содержащие '{key_word}', не найдены.")

except FileNotFoundError:
    print(f"Ошибка файл {file_name} не найден")


#-----------------------------------------------Task_#2-----------------------------------------------------------------
# Поиск и удаление дубликатов
#
# Напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.
# Имя нового файла формируется как unique_<original_filename>.
# Если файл не существует, программа должна вывести ошибку.
# Исходный порядок строк должен сохраниться.
# Если в файле нет дубликатов, создаётся точная копия файла.
# Используйте файл movies_to_watch.txt.
# Пример ввода:
#
# Введите имя файла: movies_to_watch.txt
# Пример вывода:
# Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

file_name = input("Enter file name: ")

new_file = f"unique_{file_name}"

try:
    uniq_lines = []
    with open(file_name, "r") as f:
        for line in f:
            if line not in uniq_lines:
                uniq_lines.append(line)
    if uniq_lines:
        with open(new_file, "w") as f:
            for line in uniq_lines:
                f.write(line)
except FileNotFoundError:
    print("File not found")

#-----------------------------------------------------------------------------------------------------------------------