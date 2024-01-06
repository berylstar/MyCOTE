import sys
input = sys.stdin.readline

L = int(input())
M = 1234567891
r = 31
strr = input()
 
answer = 0
 
for i in range(L):
    num = ord(strr[i]) - 96
    answer += num * (r ** i)

print(answer % M)