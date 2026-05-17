#-----------------------------------------Task_#1-----------------------------------------------------------------------
#---------------------------------------Класс Person--------------------------------------------------------------------
# Создайте класс Person, представляющий человека.
# Каждый человек должен иметь имя.
# Добавьте метод introduce(), который выводит приветствие с именем.

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f'Hello, my name is {self.name}'

#----------------------------------------Task#2-------------------------------------------------------------------------
#--------------------------------------Класс Student--------------------------------------------------------------------
# На основе класса Person создайте класс Student.
# Студент должен иметь имя и номер курса.
# Метод introduce() должен сначала выводить базовое приветствие, а затем строку: I'm on course <номер_курса>.

class Student(Person):
    def __init__(self, name, course_num):
        super().__init__(name)
        self.course_num = course_num

    def introduce(self):
        return f"{super().introduce()}. \nI'm on course {self.course_num}"

#------------------------------------------Task#3-----------------------------------------------------------------------
#--------------------------------Класс Teacher и список людей-----------------------------------------------------------
# На основе класса Person создайте класс Teacher.
# У преподавателя есть имя и предмет.
# Метод introduce() должен выводить имя и предмет.
# Метод introduce() должен выводить строку: Hello, I am professor <имя>. My subject is <предмет>.
# Создайте список, в котором будут Student и Teacher, и вызовите у всех метод introduce().

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        super().introduce()
        return f'Hello, I am professor {self.name} \nMy subject is {self.subject}'


staff = [
    Student("Alex", 3),
    Teacher("Dr. Brown", "Physics")
]

for person in staff:
    print(person.introduce())

#-----------------------------------------------------------------------------------------------------------------------