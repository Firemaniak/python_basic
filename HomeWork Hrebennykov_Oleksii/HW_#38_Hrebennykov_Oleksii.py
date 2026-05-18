#----------------------------------------Task_#1------------------------------------------------------------------------
#-------------------------------------Банковский счёт-------------------------------------------------------------------
# Создайте класс BankAccount, описывающий банковский счёт.
# Объект должен хранить имя владельца и текущий баланс.
#
# Реализуйте методы:
# пополнение счёта
# снятие средств
# отображение баланса
#
# При попытке снять больше, чем есть на счёте, операция не должна выполняться.
# Продумайте, какие поля и методы следует скрыть от внешнего доступа, а какие оставить открытыми.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Not enough money")
        self.__balance -= amount

    @property
    def show_balance(self):
        return f'Current balance: {self.__balance}'

    def __str__(self):
        return self.name

a1 = BankAccount("Alex", 100)
a1.deposit(300)
print(a1.show_balance)
try:
    print(a1.withdraw(1000))

except ValueError as error:
    print(error)
print(a1.show_balance)

#-----------------------------------------------Task_#2-----------------------------------------------------------------
print("-" * 50)
# Доработайте класс BankAccount.
#
# Каждая операция пополнения и снятия должна сохраняться в историю.
# История должна быть доступна через property history только для чтения.
# История представляется в виде списка строк ("Deposit: 150", "Withdraw: 100" и т.д.).


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.__history = []

    def deposit(self, amount):
        self.__balance += amount
        self.__history.append(f'Deposit: {amount}')

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Not enough money")
        self.__balance -= amount
        self.__history.append(f'Withdraw: {amount}')

    @property
    def show_balance(self):
        return f'Current balance: {self.__balance}'

    @property
    def history(self):
        return "Operation history:\n\t" + "\n\t".join(self.__history)

    def __str__(self):
        return self.name

a1 = BankAccount("Alex", 100)
a1.deposit(300)
print(a1.show_balance)
try:
    print(a1.withdraw(100))

except ValueError as error:
    print(error)
print(a1.show_balance)
print(a1.history)

#-----------------------------------------------------------------------------------------------------------------------