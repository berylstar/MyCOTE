import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())
    N = int(input())
    
    apart = [i for i in range(1, N + 1)]
    for _ in range(K):
        for i in range(1, N):
            apart[i] += apart[i - 1]
    print(apart[-1])