from sys import stdin
input = stdin.readline

def CheckPrime(num):
    for i in range(2, min(int(num**(0.5)) + 1, 1000001)):
        if num % i == 0:
            return False
    return True

for _ in range(int(input())):
    if CheckPrime(int(input())):
        print("YES")
    else:
        print("NO")