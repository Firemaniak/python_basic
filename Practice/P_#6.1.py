products = ["Молоко", "Хлеб", "Сахар-песок", "Подсолнечное масло", "Шоколадный батончик", "Мороженое"]
print("\n".join(products))


# Task II
"""Напишите программу, которая фильтрует список кортежей,
оставляя только те, где количество больше 10.
Выведите данные согласно примеру."""

data = [("апельсин", 5), ("вишня", 12), ("киви", 18), ("ананас", 7), ("яблоко", 20)]

for item in data:
    product, quantity = item
    if quantity > 10:
        print(f"Товар : {product} | Цена : {quantity}")


# Task III
products = [
 ("Кофе", 127.99),
 ("Чай", 52.49),
 ("Шоколад", 81.99)
]

discount = int(input("Введите процент скидки: "))

print("Название | Цена | Скидка |Итоговая цена")
for item in products:
    product, price = item
    print(f"{product:>10} | {price:>10} | {discount:>10} | {price * (1 - (discount/100)):>10}")