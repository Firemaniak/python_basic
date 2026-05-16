#----------------------------------------------------Task_#1------------------------------------------------------------
#--------------------------------------------Анализ курсов студентов----------------------------------------------------
# Реализовать программу, которая должна:
# Прочитать файл student_courses.json, содержащий:
# имя,
# дату рождения (birth_date) в формате дд.мм.гггг,
# дату поступления (enrollment_date) в том же формате,
# список курсов.
#
# Вычислить:
# Общее количество студентов.
# Средний возраст на момент поступления.
# Количество студентов на каждом курсе.
# Сохранить отчёт в JSON-файл student_courses_report.json.

import json
from datetime import datetime
from collections import Counter

with open("student_courses.json", "r", encoding="utf-8") as file:
    students = json.load(file)

total_students = len(students)
ages = []
students_per_course = Counter()

for student in students:
    birth_date = datetime.strptime(student["birth_date"], "%d.%m.%Y")
    enrollment_date = datetime.strptime(student["enrollment_date"], "%d.%m.%Y")

    age = (enrollment_date - birth_date).days / 365.25
    ages.append(age)

    students_per_course.update(student["courses"])

report = {
    "total_students": total_students,
    "average_enrollment_age": round(sum(ages) / len(ages), 1),
    "students_per_course": dict(sorted(students_per_course.items()))
}

with open("student_courses_report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4, ensure_ascii=False)

print("Report saved to student_courses_report.json")

------------------------------------------------------------------------------------------------------------------------