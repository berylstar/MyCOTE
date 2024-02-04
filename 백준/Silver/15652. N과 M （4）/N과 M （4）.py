N, M = map(int, input().split())

def DFS(c):
    if len(ret) == M:
        print(*ret)
    else:
        for k in range(c, N+1):
            ret.append(k)
            DFS(k)
            ret.pop()

ret = []

DFS(1)