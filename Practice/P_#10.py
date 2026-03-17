# Task #1
text1 = "This is a sample text with some repeated words."
text2 = "Another sample text with different words."
text3 = "Text processing is fun when words repeat."
from collections import Counter
def popular_words(*texts, n=5):
    all_words = " ".join(texts).replace('.', ' ').lower().split()
    counter = Counter(all_words)
    return counter.most_common(n)
print(f'5 самых популярных слов: ')
print(*popular_words(text1, text2, text3), sep='\n')
print(*popular_words(text1, text2, text3, n=3), sep='\n')

#Task #2
from collections import defaultdict

def group_tasks(tasks):
    grouped = defaultdict(list)
    for task, category in tasks.items():
        grouped[category].append(task)

    return dict(grouped)

tasks = {
    "task1": "работа",
    "task2": "учёба",
    "task3": "развлечения",
    "task4": "работа",
    "task5": "учёба"
}
grouped_tasks = group_tasks(tasks)
print("Группировка по категориям:")
for category, task_list in grouped_tasks.items():
    print(f"'{category}': {task_list}")

#Task #3

def find_tasks_by_category(tasks, category):

    return [task for task, cat in tasks.items() if cat == category]

tasks = {
    "task1": "работа",
    "task2": "учёба",
    "task3": "развлечения",
    "task4": "работа",
    "task5": "учёба"
}
category = "учёба"
result = find_tasks_by_category(tasks, category)

print(f"Задачи для категории '{category}':")
print(result)