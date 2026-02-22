#Task1
# Число в конце
# Напишите программу, которая создает новый список. В него необходимо добавить только те строки из исходного списка,
# в которых цифры находятся только в конце.
#
# Данные:

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
new_strings = []
for item in strings:
    if item.rstrip("0123456789").isalpha():
        new_strings.append(item)
print("Строки с цифрами только в конце: ", new_strings)

#Task2
# Удаление кратных
# Напишите программу, которая удаляет из списка все значения, кратные числу, которое вводится пользователем.
# Данные:
# #
# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
#
# Пример вывода:
# Введите число для удаления кратных ему элементов: 3
# Список без кратных значений: [1, 10, 19, 20]

a = int(input("Введите число для удаления кратных ему элементов:  "))
spisok = []
for i in numbers:
    if i % a != 0:
        spisok.append(i)
print(spisok)

#Task3
# Порядок четных
# Напишите программу, которая формирует новый список чисел. Добавьте в него все элементы исходного списка, где:
# нечетные числа занимают те же позиции,чётные числа отсортированы между собой обратном порядке.
# Данные:
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
even_list = []
result = []
even_index = 0

for item in numbers:
    if item % 2 == 0:
        even_list.append(item)
even_list.sort(reverse=True)

for item in numbers:
    if item % 2 == 0:
        result.append(even_list[even_index])
        even_index += 1
    else:
        result.append(item)
print("Начальный список: ", numbers)
print("Список после сортировки:", result)

