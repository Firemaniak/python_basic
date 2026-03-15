# Звёздочки вместо чисел
# Напишите программу, которая заменяет все цифры в строке на звёздочки *.
text = "My number is 123-456-789"
#
# Пример вывода:
# Строка: My number is 123-456-789
# Результат: My number is ***-***-***

for digit in "0123456789":
    text = text.replace(digit, '*')
print(text)

#Task #2
# Количество символов
# Напишите программу, которая подсчитывает количество вхождений всех символов в строке.
# Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр), с указанием их количества.
# Выводите повторяющиеся символы только один раз.

text = "Programming in python"

# Пример вывода:
# Строка: Programming in python
#
# Символ 'p' встречается 2 раз(а)
# Символ 'r' встречается 2 раз(а)
# Символ 'o' встречается 2 раз(а)
# Символ 'g' встречается 2 раз(а)
# Символ 'm' встречается 2 раз(а)
# Символ 'i' встречается 2 раз(а)
# Символ 'n' встречается 3 раз(а)
# Символ ' ' встречается 2 раз(а)

text = text.lower()
new_text = []
print("Строка: Programming in python")
for word in text:
    if text.count(word) > 1 and word not in new_text:
        print(f'Символ "{word}" встречается {text.count(word)} раз(а)')
        new_text.append(word)

#Task#3
# Увеличение чисел
# Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
#
# Пример вывода:
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.

text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."

result = ""
number = ""

for char in text:
    if char.isdigit():
        number += char

    elif char == "." and number != "":
        number += char

    else:
        if number != "":
            if result.endswith("...."):
                result += number
            else:
                result += str(float(number) * 10)
            number = ""

        result += char

if number != "":
    if result.endswith("...."):
        result += number
    else:
        result += str(float(number) * 10)
print(result)

