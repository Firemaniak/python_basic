# text = 'Hello'
# for letter in text:
#     print(letter, end=' ') ###ne vsegda sep delaet ' '
# from random import random

# text = 'Hello'
# for letter in text:
#     print(letter)

# text = 'Hello'
# for letter in text:
#     print(letter, end='*') ###    H*e*l*l*o*   budit





# range(start, stop, step) ### будет генерировать эллементы арифметической прогресии

# range(2,10,2) #   2 4 6 8  bez 10   ---- posledovatelnost

# range(2,10) #       2,3,4,5,6,7,8,9   ---- posledovatelnost
#
# range(10) #         0,1,2,3,4,5,6,7,8,9  - posledovatelnost


# x = 'Hello World!'
#
# for i in range(len(x)):
#     print(x[i])


# for i in range(100):
#     print(i)

# for i in range(13, 1, -2):
#     print(i) # naoborot


# x = 'Python'
# i = 0
# for item in x:
#     print(i, item, sep=', ') ### bad style
#     i += 1

# x = 'Python'
# for i in range(len(x)):
#     print(i, x[i], sep=', ') # bad style


# x = 'Python'
# i = 0
# while i < len(x):
#     print(i, x[i], sep=', ') ## bad style
#     i += 1


# x = 'Python'
#
# for i, item in enumerate(x):
#     print(i, item, sep=', ') ### good style but its leter

# x = 'Python'
# for letter in 'Python':
#     if letter == 'h':
#         break
#     print(letter)

# x = 'Python'
#
# for letter in 'Python':
#     if letter == 'h':
#         # пропускаем букву "h" и продолжаем цикл
#         continue
#     print(letter)
# else:
#     print('Finish')



# vsroenie cykly

# counter = 0
# for i in 'AB':
#     print('-' * 20)
#     for j in '12':
#         print(i, j)
# print('-' * 20)
# counter += 1
# print(counter)





