#-------------------------------------------------Task_#1---------------------------------------------------------------
#--------------------------------------------Электронное письмо---------------------------------------------------------
# Реализуйте класс Email, который представляет электронное письмо. Каждое письмо должно содержать:
#
# sender — адрес отправителя
#
# recipient — адрес получателя
#
# subject — тема письма
#
# body — текст письма
#
# date — дата отправки
#
# Класс должен поддерживать:
#
# Сравнение писем по дате
#
# Преобразование письма в строку
#
# Получение длины текста письма
#
# Проверку на наличие текста в письме или не состоит ли текст только из пробелов
#
# Пример использования:
#
# e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
# e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))
# print(e1)
# print(e1)
# print(e2)
# print("Length:", len(e1))
# print("Has text:", bool(e1))
# print("Is newer:", e2 > e1)
# Пример вывода:
#
# From: alice@example.com
# To: bob@example.com
# Subject: Meeting
# - Let's meet at 10am -
# From: bob@example.com
# From: bob@example.com
# To: alice@example.com
# Subject: Report
# -  -
# Length: 18
# Length: 18
# Has text: True
# Is newer: True


from datetime import datetime
from functools import total_ordering


@total_ordering
class Email:
    """
    Represents an email message.

    Attributes:
        sender (str): Email sender address.
        recipient (str): Email recipient address.
        subject (str): Email subject.
        body (str): Email text content.
        date (datetime): Sending date.

    Methods:
        __str__():
            Returns formatted email representation.

        __len__():
            Returns length of email body.

        __bool__():
            Checks whether the email contains text.

        __eq__():
            Compares emails by date equality.

        __lt__():
            Compares emails by date.
    """

    def __init__(self, sender, recipient, subject, body, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __str__(self):
        """
        Return formatted string representation of the email.
        """
        return (
            f"From: {self.sender}\n"
            f"To: {self.recipient}\n"
            f"Subject: {self.subject}\n"
            f"- {self.body} -"
        )

    def __len__(self):
        """
        Return length of email body.
        """
        return len(self.body)

    def __bool__(self):
        """
        Return True if email body contains non-space text.
        """
        return bool(self.body.strip())

    def __eq__(self, other):
        """
        Compare emails by equality of dates.
        """
        if not isinstance(other, Email):
            return NotImplemented

        return self.date == other.date

    def __lt__(self, other):
        """
        Compare emails by sending date.
        """
        if not isinstance(other, Email):
            return NotImplemented

        return self.date < other.date


e1 = Email(
    "alice@example.com",
    "bob@example.com",
    "Meeting",
    "Let's meet at 10am",
    datetime(2024, 6, 10)
)

e2 = Email(
    "bob@example.com",
    "alice@example.com",
    "Report",
    "",
    datetime(2024, 6, 11)
)

print(e1)
print()

print(e2)
print()

print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)

#---------------------------------------------Task_#2-------------------------------------------------------------------
#------------------------------------Класс для работы с деньгами--------------------------------------------------------
# Создайте класс Money, в котором можно:
#
# складывать и вычитать объекты через операторы + и -
# выводить объект как строку в виде "$<amount>"
# при сложении и вычитании возвращается новый объект
# если вычитание приводит к отрицательному значению — вернуть 0

# Пример использования:
#
# money1 = Money(100)
# money2 = Money(50)
# print(money1 + money2)
# print(money1 + money2)
# print(money1 - money2)
# print(money2 - money1)
# Пример вывода:
#
# $150
# $50
# $0

class Money:
    """
    Represents a money amount.

    Attributes:
        amount (int | float): Money value.

    Methods:
        __add__():
            Adds two Money objects.

        __sub__():
            Subtracts two Money objects.

        __str__():
            Returns formatted money string.
    """

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):

        if not isinstance(other, Money):
            return NotImplemented

        return Money(self.amount + other.amount)

    def __sub__(self, other):

        if not isinstance(other, Money):
            return NotImplemented

        result = self.amount - other.amount

        if result < 0:
            result = 0

        return Money(result)

    def __str__(self):
        return f"${self.amount}"


money1 = Money(100)
money2 = Money(50)

print(money1 + money2)
print(money1 - money2)
print(money2 - money1)

#-----------------------------------------------------------------------------------------------------------------------