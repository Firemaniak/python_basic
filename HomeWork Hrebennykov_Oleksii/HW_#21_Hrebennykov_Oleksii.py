#---------------------------------------------Task_#1-------------------------------------------------------------------
# Повторения букв
# Реализуйте функцию, которая принимает текст и возвращает словарь с подсчётом количества каждой буквы, игнорируя регистр.
#
# Данные:
# text = "Programming is fun!"
#
# Пример вывода:
# {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}

text = "Programming is fun!"
# result = {}
# for item in text.lower():
#     if item.isalpha():
#         if item in result:
#             result[item] += 1
#         else:
#             result[item] = 1
#
# print(result)

def count_char(text):
    result = {}
    for item in text.lower():
        if item.isalpha():
            if item in result:
                result[item] += 1
            else:
                result[item] = 1
    return result

print(count_char(text))
#-----------------------------------------------------------------------------------------------------------------------
from collections import defaultdict

def co_char(text):
    result = defaultdict(int)
    for item in text.lower():
        if item.isalpha():
            result[item] += 1
    return result
print(dict(co_char(text)))

#-----------------------------------------------------------------------------------------------------------------------
from collections import Counter

def counter_char(text):
    return(dict(Counter(item for item in text.lower() if item.isalpha())))
print(counter_char(text))

#------------------------------------------Task_#2----------------------------------------------------------------------
# Группировка студентов по классам
#
# Создайте структуру для группировки студентов по классам.
# Добавьте студентов в соответствующие группы.
#
# Данные:
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

# Пример вывода:
# {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}

def class_group(students):
    result = defaultdict(list)
    for group, student in students:
        result[group].append(student)
    return dict(result)

print(class_group(students))
