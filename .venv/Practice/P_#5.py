# Задача: Напишите программу, которая принимает строку с числами через пробел и
# выводит сумму всех чисел.
# Пример вывода: Введите список чисел через пробел: 1 2 3 4 5
# Сумма чисел: 15

digits = input("Введите список цифр через пробел: ").split()
sum_of_digits = 0
for i in digits:
    sum_of_digits += int(i)

print(sum_of_digits)

#number = input("Enter a number: ")
rev = number.split()
num =[]
for i in rev:
    num.append(int(i))
num.reverse()
print(num)


number = input("Enter a number: ")
num = list(map(int, number.split()))
print(num[::-1])


numbers = [-1, 8, 2, 0, -3, -9, -1, 10, 7, -4]
pos = 0
neg = 0
for i in numbers:
    if i % 2 == 0:
        pos += i
    else:
        neg += i
print ("Изначальный список: [-1, 8, 2, 0, -3, -9, -1, 10, 7, -4]",
       f"Сумма чётных: {pos}",
       f"Сумма нечётных: {neg}", sep="\n")


# Задача: Напишите программу, которая выводит наибольшее число в списке, не
# используя встроенную функцию max(), а также его индекс в списке.
# Данные: numbers = [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
# Пример вывода: Список чисел: [3, 12, 8, 22, 9, 25, 6, 23, 8, 7] Наибольшее число: 25
# Индекс числа: 5

numbers = [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
index_max = 0
max_num = 0
for i in range(len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]
        index_max = i
print("Наибольшее число: ", max_num)
print("Индекс числа: ", index_max)


numbers = [1, 2, 3, 4, 5]
print(f"Изначальный список:"f"{numbers}")
for i in range(0, len(numbers)-1, 2):
    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print(f"Список после перестановки:"f"{numbers}")


text = "apple 42 banana 3 100 orange"
print (text)
listt = text.split()
sp = []
for item in listt:
   if item.isdigit():
       sp.append(int(item))
   else:
       sp.append(item.capitalize())
print(sp)


text = input()
encode = ""
rep = 1
for i in range(1,len(text)):
    if text[i] == text[i-1]:
        rep += 1
    else:
        encode += text[i-1] + str(rep)
        rep = 1
encode += text[-1] + str(rep)
print(encode)