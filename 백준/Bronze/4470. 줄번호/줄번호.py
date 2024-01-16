from sys import stdin
input = stdin.readline

for i in range(int(input())):
    print("{0}.".format(i+1), input().rstrip())