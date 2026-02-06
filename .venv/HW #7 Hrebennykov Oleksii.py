import random

secret = random.randint(1, 100)
ATTEMPTS = 10
ifwin = True
i = 0

while i < ATTEMPTS:
    user_number = int(input("Enter a number: "))
    i += 1
    if user_number == secret:
        print("Correct!")
        print('You use ', i, 'attempts')
        break
    elif user_number < secret:
        print("Your number is too low!")
    else:
        print("Your number is too high!")
else:
    iswin = False
    print('You lose')

if iswin:
......