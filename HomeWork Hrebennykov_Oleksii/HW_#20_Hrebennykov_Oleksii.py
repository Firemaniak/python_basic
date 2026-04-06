#-------------------------------------------------------#Task_#1--------------------------------------------------------
# Простое число
# Напишите функцию, которая проверяет, является ли число n простым (делится только на 1 и само себя)
# и возвращает булевый результат.
# Данные:
# n = 17
# Пример вывода:
# Число 17 является простым

n = 17
def simple_num (n):
    if n < 2:
        return False
    for i in range(2, n):
        if n / i == 0:
            return False
        else:
            return True

if simple_num(n):
    print(f"Число {n} является простым")
else:
    print(f'Число {n} не является простым')

#---------------------------------------------------Task_#2-------------------------------------------------------------
# Фильтрация чисел по чётности
# Напишите функцию, которая принимает filter_type ("even" или "odd") и произвольное количество чисел,
# возвращая только те, которые соответствуют фильтру.
#
# Пример вызова:
# print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
# print(filter_numbers("odd", 10, 15, 20, 25))
# print(filter_numbers("prime", 2, 3, 5, 7))
#
# Пример вывода:
# [2, 4, 6]
# [15, 25]
# Некорректный фильтр

def filter_numbers(filter_type, *numbers):
    result = []
    for n in numbers:
        if filter_type == 'even' and n % 2 == 0:
            result.append(n)
        elif filter_type == 'odd' and n % 2 != 0:
            result.append(n)
        elif filter_type == 'prime':
            if n > 1:
                is_prime = True
                for i in range(2, n):
                    if n % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    result.append(n)

    if filter_type not in ['even', 'odd', 'prime']:
        return "Некорректный фильтр"

    return result

print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

#--------------------------------------------Task_#3-------------------------------------------------------------------
# Объединение словарей
# Напишите функцию, которая принимает любое количество словарей и объединяет их в один.
# Если ключи повторяются, используется значение из последнего словаря.
#
# Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

# Пример вызова:
# print(merge_dicts(dict1, dict2, dict3))
#
# Пример вывода:
# {'a': 1, 'b': 3, 'c': 4, 'd': 5}

def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            result[key] = value
    return result
print(merge_dicts(dict1,dict2,dict3))

