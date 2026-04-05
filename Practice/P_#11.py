from typing import Callable
nums = [1, 2, 3, 4, 5, 6]

def even_or_not(n: int):
    return n % 2 == 0

def filter_list(predicate: Callable, elements: list[int]):
    result = []
    for item in elements:
        if predicate(item):
            result.append(item)
    return result

print(filter_list(even_or_not, nums))


----------------------------------------------------------------------------------

nums = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda n: n % 2 == 0, nums))

print(result)

--------------------------------------------------------------------------

words = ["hi", "Hello", "a", "python", "Ok"]
min_len = 1

def filter_long_words(data):
    return list(filter(lambda x: len(x) > min_len, data))

print(filter_long_words(words))

--------------------------------------------------------------------------

words = ["hi", "Hello", "a", "python", "Ok", "Radar"]


def filter_long_words(data, criterion):
    return list(filter(criterion, data))

result_upper = filter_long_words(words, lambda x: x[0].isupper())
print(result_upper)

result_one_symbol = filter_long_words(words, lambda x: len(x) == 1)
print(result_one_symbol)

result_same_letter = filter_long_words(words, lambda x: x[0].lower() == x[-1].lower())
print(result_same_letter)

---------------------------------
words = ["apple", "banana", "kiwi", "grape"]

def sort_by_length(data):
    return sorted(data, key=len)

print(sort_by_length(words))

----------------------------------------------------------------
tasks = {"task1": 5, "task2": 3, "task3": 7, "task4": 2}
time_limit = 10

def filter_task_by_limit(data, limit):
    sorted_tasks = sorted(data.items(), key=lambda x: x[1], reverse=True)

    result = {}
    current_sum = 0

    for task, time in sorted_tasks:
        if current_sum + time <= limit:
            result[task] = time
            current_sum += time

    return result

filtered = filter_task_by_limit(tasks, time_limit)
print(filtered)