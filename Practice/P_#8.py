"""
Список квадратов
Создайте список, содержащий квадраты всех чётных чисел из диапазона от 1 до
заданного пользователем числа включительно.
Пример вывода:
Введите конец диапазона: 20
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
"""
# user_input = int(input("Введите число: "))
# res = [num ** 2 for num in range(2, user_input + 1, 2)]
# print(res)


"""
Фильтрация по символу
Создайте новый список, исключив все строки, содержащие введённый
пользователем символ.
Данные:
words = ["apple", "cherry", "kiwi", "banana", "orange"]
Пример вывода:
Исключить символ: r
['apple', 'kiwi', 'banana']
"""
# user_input = input("Введите символ:")
#
# words = ["apple", "cherry", "kiwi", "banana", "orange"]
#
# res = [word for word in words if user_input not in word]
# print(res)


"""
База данных обитателей джунглей
Данные:
animals = ["тигр", "слон", "обезьяна", "змея"]
weights = [250, 4000, 15, 5]
Пример вывода:
['Тигр весит 250 кг', 'Слон весит 4000 кг', 'Обезьяна весит 15 кг', 'Змея весит
5 кг']
Самое лёгкое животное: змея

"""
# animals = ["тигр", "слон", "обезьяна", "змея"]
# weights = [250, 4000, 15, 5]
#
# res = [f"{animal.title()} весит {weight} кг" for animal, weight in zip(animals, weights)]
# weight_calculate = [animal for animal, weight in zip(animals, weights) if min(weights) == weight]
#
# print(res)
# print(f"Самое легкое животное: {weight_calculate[0]}")

"""
Группы слов
Группируйте слова по длине в обратном порядке, отсортированные по алфавиту
внутри группы.
Данные:
words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]
Пример вывода:
Группы слов: [['banana', 'cherry'], ['apple', 'grape', 'melon'], ['kiwi',
'pear']]
"""
# words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]

# list_length = set([len(item) for item in words])
# grouped_words = []
# for length in list_length:
#     tmp = []
#     for item in reversed(words):
#         if len(item) == length:
#             tmp.append(item)
#             words.remove(item)
#     tmp.sort()
#     grouped_words.append(tmp)
#
# print(grouped_words)


"""
Распаковка матрицы

Создайте список, содержащий все элементы двумерной матрицы в одном
измерении.
Данные:
matrix = [[1, 2], [3, 4], [5, 6]]
Пример вывода:
[1, 2, 3, 4, 5, 6]
"""
# new_list = [expression for item1 in iterable1 for item2 in iterable2]

# matrix = [[1, 2], [3, 4], [5, 6]]

# res_list = []
# for i in matrix:
#     for j in i:
#         res_list.append(j)
# print(res_list)
#
# res = [j for i in matrix for j in i]
# print(res)

# new_list = []
# for row in matrix:
#     new_list.extend(row)
# print(new_list)

"""
Координатная сетка
Создайте список всех возможных координат на квадратной сетке размером n x n.
Пример вывода:
Введите размер координатной сетки: 3
Координаты: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
"""

# new_list = [expression for item1 in iterable1 for item2 in iterable2]

# user_num = int(input("Введите размер координатной сетки: "))
# res = [(row, column) for row in range(user_num) for column in range(user_num)]
# print(res)

"""
Сравнение матриц
Проверьте, совпадают ли диагональные элементы двух квадратных матриц
одинакового размера.
Данные:

Совпадают ли главные диагонали: True
Совпадают ли побочные диагонали: True
"""

# matrix1 = [[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]]
# matrix2 = [[1, 0, 3],
#            [0, 5, 0],
#            [7, 0, 9]]
#
# matrix_length_1 = len(matrix1)
#
# flag_1 = True
#
# for i in range(matrix_length_1):
#     if matrix1[i][i] != matrix2[i][i]:
#         flag_1 = False
#         break
#
# print(flag_1)
#
# flag_2 = True
#
# for i in range(matrix_length_1):
#     if matrix1[i][matrix_length_1 - 1 - i] != matrix2[i][matrix_length_1 - 1 - i]:
#         flag_2 = False
#         break
#
# print(flag_2)

"""
Подсчёт уникальных слов
Напишите программу, которая принимает строку текста, разделённого пробелами, и
определяет количество уникальных слов.
Данные:

Пример вывода:
Количество уникальных: 3
"""

# text = "Apple orange apple banana Orange".lower()
#
# res = set(text.split())
#
# print(f"Количество уникальных: {len(res)}")


"""
Проверка, состоят ли два списка чисел из одинаковых цифр (независимо от
порядка).
Данные:

Пример вывода:
True
"""

# list1 = [1, 2, 3, 4, 4]
# list2 = [4, 3, 2, 1, 1]
#
# print(set(list1) == set(list2))


"""
Охота за сокровищами
Определение различий и пересечений между двумя наборами драгоценностей.
Данные:

Пример вывода:
Только в первом сундуке: {'золото', 'алмазы'}
Общее в обоих сундуках: {'серебро', 'рубины'}
Все уникальные драгоценности: {'золото', 'серебро', 'рубины', 'алмазы',
'изумруды', 'сапфиры'}
"""

# chest1 = {"золото", "серебро", "рубины", "алмазы"}
# chest2 = {"серебро", "рубины", "изумруды", "сапфиры"}
#
# print(f"Только в первом сундуке: {chest1.difference(chest2)}")
# print(f"Общее в обоих сундуках: {chest1.intersection(chest2)}")
# print(f"Все уникальные драгоценности: {chest1.union(chest2)}")
