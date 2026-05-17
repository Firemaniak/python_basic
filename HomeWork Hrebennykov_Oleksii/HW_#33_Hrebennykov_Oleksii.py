#----------------------------------------------Task_#1------------------------------------------------------------------
#---------------------------------------Среднее время выполнения--------------------------------------------------------
# Создайте декоратор measure_time, который измеряет и выводит среднее время выполнения функции за 5 вызовов.
# Функция может быть любой: например, сортировка списка, чтение из файла или расчёты.

import time
import functools

def measure_time(func):
    """
    Measure average execution time of a function over 5 runs.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        total_time = 0
        result = None

        for _ in range(5):
            start_time = time.time()

            result = func(*args, **kwargs)

            end_time = time.time()

            total_time += end_time - start_time

        average_time = total_time / 5

        print(f"Среднее время выполнения для 5 вызовов: {average_time:.2f} секунд")

        return result

    return wrapper

@measure_time
def compute():
    total = 0

    for i in range(10_000_000):
        total += i

    return total

result = compute()
print(f"Результат: {result}")

#----------------------------------------------Task#2-------------------------------------------------------------------
#--------------------------Среднее время выполнения с количеством вызовов-----------------------------------------------

# Доработайте декоратор measure_time, чтобы он принимал параметр repeats — количество вызовов функции.
# Декоратор должен выполнять функцию указанное число раз и выводить среднее время выполнения.

import time
import functools

def measure_time(repeats):
    """
    Decorator factory that measures average execution time.
    """

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            result = None

            for _ in range(repeats):
                start_time = time.time()

                result = func(*args, **kwargs)

                end_time = time.time()

                total_time += end_time - start_time

            average_time = total_time / repeats

            print(
                f"Среднее время выполнения для {repeats} вызовов: "
                f"{average_time:.2f} секунд"
            )

            return result

        return wrapper

    return decorator

@measure_time(10)
def compute():
    total = 0

    for i in range(10_000_000):
        total += i

    return total

result = compute()
print(f"Результат: {result}")

#-----------------------------------------------------------------------------------------------------------------------