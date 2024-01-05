import math
number = math.factorial(int(input()))

for i, v in enumerate(str(number)[::-1]):
    if v != '0':
        print(i)
        break