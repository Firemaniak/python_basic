#---------------------------------------------------Task_#1-------------------------------------------------------------
#                                                 Выбор заказов
# У вас есть список заказов. Каждый заказ содержит название продукта и его цену.
# Напишите функцию, которая:
# Отбирает заказы дороже 500.
# Создаёт список названий отобранных продуктов в алфавитном порядке.
# Возвращает итоговый список названий.
from itertools import product

# Данные:

orders = [

    {"product": "Laptop", "price": 1200},

    {"product": "Mouse", "price": 50},

    {"product": "Keyboard", "price": 100},

    {"product": "Monitor", "price": 300},

    {"product": "Chair", "price": 800},

    {"product": "Desk", "price": 400}

]

# Пример вывода:
# ['Chair', 'Laptop']

# def price_filter(orders):
#     result = []
#     for order in orders:
#         if order["price"] > 500:
#             result.append(order["product"])
#
#     result.sort()
#     return result
# print(price_filter(orders))
#-----------------------------------------------------------------------------------------------------------------------
def filter_price(orders):
    filtered = filter(lambda order: order["price"] > 500, orders)
    mapping = map(lambda order: order["product"], filtered)
    return sorted(mapping)

print(filter_price(orders))
#-----------------------------------------------------------------------------------------------------------------------
def filter_p(orders):
    return sorted(map(lambda o: o["product"], filter(lambda o: o["price"] > 500, orders)))
print(filter_p(orders))

#--------------------------------------------Task_#2--------------------------------------------------------------------
#------------------------------------------Статистика продаж------------------------------------------------------------
# Дан список продаж в виде кортежей (товар, количество, цена).
# Напишите программу, которая:
# Вычисляет общую выручку для каждого товара.
# Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
# Данные:
sales = [

    ("Laptop", 5, 1200),

    ("Mouse", 50, 20),

    ("Keyboard", 30, 50),

    ("Monitor", 10, 300),

    ("Chair", 20, 800)

]
# Пример вывода:
# {'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}

def calcul_prod(sales):
    result = {}
    for name, q_ty, price in sales:
        result[name] = result.get(name, 0) + q_ty * price
    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
print(calcul_prod(sales))