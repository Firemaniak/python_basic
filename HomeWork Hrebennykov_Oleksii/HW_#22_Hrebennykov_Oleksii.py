def greetings (name):
    return f'Hello, {name}'
print(greetings ('Alex'))

x = greetings
print(x('Alex'))

def filter_odd (numbers):
    res = []
    for item in numbers:
        if item % 2:
            res.append(item)
    return res

a = [1, 3 , 4 , 6, 8, 11 ,-111110 , -111]
b = filter_odd(a)
print(b)

