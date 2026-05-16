#--------------------------------------------Task_#1--------------------------------------------------------------------
#-----------------------------------Фабрика функций округления----------------------------------------------------------
# Создайте функцию make_rounder(), которая принимает количество знаков для округления и возвращает другую функцию.
# Полученная функция должна принимать число и возвращать его, округлённое до указанного ранее количества знаков после запятой.
#
# Пример вызова:
#
# print(round2(3.14159))
#
# print(round2(2.71828))
#
# print(round0(9.999))
#
# Пример вывода:
#
# 3.14
#
# 2.72
#
# 10.0

def make_rounder(digits):
    """
    Create a rounding function with a fixed number of decimal places.
    """

    def round_number(number):
        return round(number, digits)

    return round_number

round2 = make_rounder(2)
round0 = make_rounder(0)

print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))

#---------------------------------------------Task#2--------------------------------------------------------------------
from datetime import datetime

def create_logger():
    """
    Create an event logger that stores messages with timestamps.
    """

    events = []

    def log(message=None):
        if message:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            events.append(f"{message}: {current_time}")

        return events

    return log

log = create_logger()

log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")

for event in log():
    print(event)

#--------------------------------------------Task#3---------------------------------------------------------------------
def frame(func):
    """
    Decorator that prints a frame around function output.
    """

    def wrapper():
        print("-" * 50)
        func()
        print("-" * 50)

    return wrapper

@frame
def say_hello():
    print("Привет, игрок!")

say_hello()

#-----------------------------------------------------------------------------------------------------------------------