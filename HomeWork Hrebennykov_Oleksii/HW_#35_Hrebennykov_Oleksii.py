#---------------------------------------------Task_#1-------------------------------------------------------------------
#----------------------------------------Счётчик экземпляров------------------------------------------------------------
#
# Создайте класс User, представляющий пользователя.
# При создании должны указываться логин (username) и пароль (password).
# У класса должно быть поле total_users, хранящее общее количество созданных пользователей.
# При каждом создании нового объекта User, счётчик должен увеличиваться.
# Добавьте метод get_total(), возвращающий количество пользователей.
# Проверьте, что счётчик работает.

class User:
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls):
        return f'Total users: {cls.total_users}'

User.get_total()
u1 = User('Alex', 123)
u2 = User('Oleh', 456)
u3 = User('Anton', 789)

print(User.get_total())
print(u1.get_total())

#--------------------------------------------Task_#2--------------------------------------------------------------------
#----------------------------------Проверка данных пользователя---------------------------------------------------------
# Доработайте класс User.
# Добавьте валидации полей при создании.
# Имя должно быть непустой строкой.
# Пароль должен быть строкой длиной не менее 5 символов.
# Если данные некорректны — выбрасывайте ValueError.
# Добавьте строковое представление объекта.
# Проверьте работу класса с разными значениями.

class User:
    total_users = 0

    def __init__(self, username, password):

        if not isinstance(username, str) or username.strip() == "":
            raise ValueError("Username cannot be an empty string")
        if not isinstance(password, str) or len(password) < 5:
            raise ValueError(f"user: {username} --> \nPassword must be at least 5 characters")

        self.username = username
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls):
        return f'Total users: {cls.total_users}'

    def __str__(self):
        return f'Username: {self.username}'

try:
    u1 = User('Alex', '123')
    u2 = User('Oleh', '45645')
    u3 = User('Anton', '78965')

    print(User.get_total())
    print(u1.get_total())
    print(u1)

except ValueError as error:
    print(f"ValueError: {error}")

#-----------------------------------------------------------------------------------------------------------------------



