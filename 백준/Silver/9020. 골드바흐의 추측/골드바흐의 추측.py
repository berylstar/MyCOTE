from sys import stdin
input = stdin.readline

def IsPrime(num):
    for k in range(2, int(num**(0.5)) + 1):
        if num % k == 0:
            return False
    return True

for _ in range(int(input())):
    num = int(input()) // 2
    for i in range(num):
        if IsPrime(num - i) and IsPrime(num + i):
            print(num - i, num + i)
            break