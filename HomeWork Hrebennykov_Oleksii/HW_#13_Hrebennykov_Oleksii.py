#Task #1
# Прогрессия увеличения
# Напишите программу, которая создаёт новый кортеж, состоящий из элементов изначального в том же порядке.
# Добавить в него только элементы, которые больше всех предыдущих значений в исходном кортеже.
#
# Данные:
# numbers = (3, 7, 2, 8, 5, 10, 1)
# Пример вывода:
# Кортеж по возрастанию: (3, 7, 8, 10)
from itertools import count

numbers = (3, 7, 2, 8, 5, 10, 1)

result = []
max_num = 0

for item in numbers:
    if item > max_num:
        result.append(item)
        max_num = item
print(tuple(result))


#Task #2
# Повторяющиеся элементы.
# Напишите программу, которая находит индексы элементов кортежа, встречающихся более одного раза.
# Вывести сами элементы и их индексы.
#
# Данные:
# numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
#
# Пример вывода:
# Индексы элемента 2: 1 4 9
# Индексы элемента 3: 2 6
# Индексы элемента 4: 3 8

numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)

printed = []

for item in numbers:
    if numbers.count(item) > 1 and item not in printed:
        print(f"Индексы элемента {item}:", end=" ")

        for i, num in enumerate(numbers):
            if num == item:
                print(i, end=" ")
        print()
        printed.append(item)

