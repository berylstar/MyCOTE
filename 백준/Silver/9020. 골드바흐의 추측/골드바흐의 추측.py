from sys import stdin
input = stdin.readline

def Prime(num):
    for k in range(2, int(num**(0.5)) + 1):
        if num % k == 0:
            return False
    return True

for _ in range(int(input())):
    num = int(input())
    half = num // 2
    for i in range(half):
        if Prime(half - i) and Prime(half + i):
            print(half - i, half + i)
            break