#----------------------------------------------Task#1-------------------------------------------------------------------
#-----------------------------------------План по дням недели----------------------------------------------------------
# Напишите программу, которая помогает планировать дела.
# Программа должна бесконечно выводить план на следующий день недели, пока пользователь нажимает 'Enter'.
#
# Данные:
#
# # Расписание дел на неделю

weekly_schedule = {

    "Monday": ["Gym", "Work", "Read book"],

    "Tuesday": ["Meeting", "Work", "Study Python"],

    "Wednesday": ["Shopping", "Work", "Watch movie"],

    "Thursday": ["Work", "Call parents", "Play guitar"],

    "Friday": ["Work", "Dinner with friends"],

    "Saturday": ["Hiking", "Rest"],

    "Sunday": ["Family time", "Rest"]

}

# Пример ввода:
#
# Нажмите 'Enter' для получения плана:
# Monday: Gym, Work, Read book
# Нажмите 'Enter' для получения плана:
# Tuesday: Meeting, Work, Study Python
# ...
# Нажмите 'Enter' для получения плана:
# Sunday: Family time, Rest
# Нажмите 'Enter' для получения плана:
# Monday: Gym, Work, Read book
# Нажмите 'Enter' для получения плана: q
# ...

from itertools import cycle

schedule_iterator = cycle(weekly_schedule.items())

while True:
    user_input = input("Нажмите 'Enter' для получения плана: ")

    if user_input.lower() == "exit":
        break

    day, tasks = next(schedule_iterator)

    print(f"\n{day}: {', '.join(tasks)}\n")

#--------------------------------------------Task #2--------------------------------------------------------------------
#---------------------------------Объединение списков продуктов---------------------------------------------------------

# Напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор,
# содержащий все продукты в нижнем регистре.
# Выведите содержимое генератора.

#Данные:
fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

# Пример вывода:
#
# apple
#
# banana
#
# orange
#
# carrot
#
# tomato
#
# cucumber
#
# milk
#
# cheese
#
# yogurt

from itertools import chain

def products_generator(*lists):
    return (product.lower() for product in chain(*lists))

products = products_generator(fruits, vegetables, dairy)

for product in products:
    print(product)


#----------------------------------------------Task#3-------------------------------------------------------------------
#-----------------------------------------Комбинации одежды-------------------------------------------------------------

# Напишите функцию, которая принимает списки типов одежды, цветов и размеров, а затем генерирует все возможные комбинации
# в формате "Clothe - Color - Size".

#Данные:

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

# Пример вывода:
#
# T-shirt - Red - S
#
# T-shirt - Red - M
#
# T-shirt - Red - L
#
# T-shirt - Blue - S
#
# ...
#
# Jacket - Black - L

from itertools import product

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]


def generate_outfits(clothes, colors, sizes):
    return (
        f"{clothe} - {color} - {size}"
        for clothe, color, size in product(clothes, colors, sizes)
    )

outfits = generate_outfits(clothes, colors, sizes)

for outfit in outfits:
    print(outfit)

#-----------------------------------------------------------------------------------------------------------------------