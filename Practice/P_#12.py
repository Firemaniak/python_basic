#-------------------------------------------Task_1-----------------------------------------------
# Сумма чисел списка
# Напишите рекурсивную функцию, которая вычисляет сумму всех чисел в списке.
# Функция должна проверять:
# ● Аргумент должен быть списком.
# ● Все элементы списка должны быть числами.
# Если данные не валидны необходимо выбрасывать исключение. При вызове функции обработайте
# возможное исключение.
# Данные
# numbers = [1, 2, 3, 4, 5]
# Пример вывода
# 15

# def sum_numbers(numbers, index = 0):
#     if not isinstance(numbers, list):
#         raise TypeError("Не список")
#     if index == len(numbers):
#         return 0
#     if not isinstance(numbers[index], int | float):
#         raise TypeError(f"Эллемент с индексом {index - 1} не является числом")
#     return numbers[index] + sum_numbers(numbers, index + 1)
#
# print(sum_numbers(numbers))

#------------------------------------------Task_2----------------------------------------------------------------------
# Реверс строки
# Напишите рекурсивную функцию, которая переворачивает строку. Если передан не строковый тип, выбросить
# исключение. При вызове функции обработайте возможное исключение.
# Данные
# text = "recursion"
# Пример вывода
# noisrucer

# def revers_string(text):
#     if not isinstance(text, str):
#         raise TypeError("Это не строка")
#     if len(text) <= 1:
#         return text
#     return text[-1] + revers_string(text[:-1])
#
# print(revers_string(text))

#--------------------------------------------Task_3------------------------------------------------------------------
# Реверс строки
# Глубина вложенности списка
# Напишите рекурсивную функцию, которая определяет максимальную глубину вложенности списка. Функция
# должна проверять:
# ● Аргумент должен быть списком.
# ● Вложенные структуры, если они есть, также должны быть списками.
# Если данные не валидны необходимо выбрасывать исключение. При вызове функции обработайте
# возможное исключение.
# Данные
# nested_list = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9]]
# Пример вывода
# Максимальная глубина: 5
# def deep_list(nested_list):
#     if not isinstance(nested_list, list):
#         raise TypeError("Это не строка")
#     deep_q_ty = 0
#     for item in nested_list:
#         if isinstance(item, list):
#             deep_a = deep_list(item)
#             if deep_a > deep_q_ty:
#                 deep_q_ty = deep_a
#     return 1 + deep_q_ty
# print(deep_list(nested_list))

#------------------------------------------Task_4--------------------------------------------------------------------
# Сумма продаж
# Есть дерево подразделений внутри компании (каждое подразделение может содержать «дочерние» отделы).
# Напишите рекурсивную функцию, которая подсчитывает суммарные продажи для всех отделов. Функция должна
# проверять:
# ● Аргумент должен быть словарем.
# ● Дочерние отделы (если есть) должны быть списком словарей.
# Если данные не валидны необходимо выбрасывать исключение. При вызове функции обработайте
# возможное исключение.
# Пример вывода
# Общая сумма продаж: 1140

company_structure = {
    "dept_name": "Head Office",
    "sales": 100,
    "sub_departments": [
        {
            "dept_name": "Sales Department",
            "sales": 200,
            "sub_departments": [
                {
                    "dept_name": "B2B Sales",
                    "sales": 120,
                }
            ]
        },
        {
            "dept_name": "IT Department",
            "sales": 150,
            "sub_departments": [
                {
                    "dept_name": "DevOps",
                    "sales": 300,
                    "sub_departments": [
                        {
                            "dept_name": "Cloud Infrastructure",
                            "sales": 180,
                        }
                    ]
                },
                {
                    "dept_name": "QA Department",
                    "sales": 90,
                }
            ]
        }
    ]
}

def calculate_sales(data):
    if not isinstance(data, dict):
        raise TypeError("Аргумент должен быть словарем")

    sales = data.get("sales", 0)
    sub_depts = data.get("sub_departments", [])

    if not isinstance(sub_depts, list):
        raise TypeError("Дочерние отделы должны быть списком")
    return sales + sum(calculate_sales(dept) for dept in sub_depts)

print(calculate_sales(company_structure))












