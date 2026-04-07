numbers = [1, 2, 3, 4]
# Каждый элемент списка возводится в квадрат
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16]

numbers = [1, 2, 4, 5, 7, 9, 10, 11]
# Из списка выбираются только чётные числа
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4, 10]

from functools import reduce
numbers = [1, 2, 3, 4]
# Умножение всех элементов списка последовательно
result = reduce(lambda x, y: x * y, numbers)
print(result)  # 24