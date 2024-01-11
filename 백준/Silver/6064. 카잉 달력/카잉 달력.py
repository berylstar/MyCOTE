import sys
input = sys.stdin.readline

def Ret(M, N, x, y):
    answer = x
    while answer <= M * N:
        if (answer - x) % M == 0 and (answer - y) % N == 0:
            return answer
        answer += M
    return -1

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    print(Ret(M, N, x, y))