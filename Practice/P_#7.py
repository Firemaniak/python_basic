# Номер
# Дан список покупок. Найдите какой по счету (начиная с единицы) товар с названием "Milk". Если товара нет,
# выведите сообщение об отсутствии.
# Данные:
# products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]
# Пример вывода:
# Товар "Milk" в списке покупок: 4


    # products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]
    # for index, elem in enumerate(products, 1):
    #     if elem == "Milk":
    #         print("Товар 'Milk' в списке покупок: ", index)
    #         break
    # else:
    #     print("Товара нет")

# Список
# Дан текст. Программа должна:
# ● Разбить текст на слова.
# уникальных
# ● Создать список уникальных слов в алфавитном порядке (не учитывая регистр).
# ● Вывести количество уникальных слов.
# Данные:
# text = "Python is a great programming language. Python is popular and powerful."
# Пример вывода:
# Количество уникальных слов: 9
# Уникальные слова: ['a', 'and', 'great', 'is', 'language', 'popular', 'powerful', 'programming',
# 'python']




#task 2
# text = "Python is a great programming language. Python is popular and powerful.".lower()
# text_list = []
# text = text.replace(".", "")
# text_split = text.split()
# for elem in text_split:
#     if elem not in text_list:
#         text_list.append(elem)
# text_list.sort()
# print("Количество уникальных слов: ",len(text_list))
# print(text_list)


#task3
# sentence = "Programming in Python is both fun and educational"
# split_sens = sentence.split()
# max_text = max(split_sens, key=len)
# print("Самое длинное слово: ", max_text)
# print("Длина слова: ", len(max_text))

#task4
# Напишите программу, которая перемещает все элементы списка, меньше 5, в конец списка, сохраняя порядок
# остальных элементов.
# Данные:
# numbers = [4, 7, 1, 6, 3, 8, 2]
# Пример вывода:
# Перемещённые элементы: [6, 7, 8, 4, 1, 3, 2]

# Суммы
# Напишите программу, которая обрабатывает список чисел и возвращает новый список, содержащий все
# возможные суммы пар разных элементов без дубликатов значений. Результат должен быть отсортирован по
# убыванию.
# Данные:
numbers = [3, 5, 9]
# Пример вывода:
# Суммы пар чисел по убыванию: [14, 12, 8]

for i in numbers:






    numbers = [4, 7, 1, 6, 3, 8, 2]
    number2 = []
    for num in numbers:
        if num < 5:
            numbers.remove(num)
            numbers.append(num)
    print(numbers)


numbers = [3, 5, 9]
number = []
for num in range(len(numbers)):
    for num2 in range(num + 1, len(numbers)):
        number.append(numbers[num] + numbers[num2])
revers_numb = sorted(number,reverse=True)
print(revers_numb)



shopping_list = [
                ("Bread", 1.20),
                ("Milk", 0.99),
                ("Eggs", 2.50),
                ("Butter", 3.75),
                ("Cheese", 4.10),
                ("Apple", 0.50)
                ]
budget = float(input("Введите ваш бюджет: "))
cost = 0
for name, price in shopping_list:
    if price <= budget:
        budget = budget - price
        cost += price
    else:
        continue
    print (f"{name}: ${price:.2f}")
print (f"Итоговая стоимость: ${cost:.2f}")


