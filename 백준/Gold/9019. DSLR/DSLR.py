from sys import stdin
input = stdin.readline

from collections import deque

def TurnLeft(num):
    first = num // 1000
    num %= 1000
    return num * 10 + first

def TurnRight(num):
    last = num % 10
    num //= 10
    return 1000 * last + num

def BFS(start, target):
    visited = [False for _ in range(10001)]
    visited[start] = True

    Q = deque()
    Q.append((start, ''))

    while Q:
        curr, msg = Q.popleft()
        
        if curr == target:
            return msg
        
        now = (curr * 2) % 10000
        if not visited[now]:
            Q.append((now, msg + 'D'))
            visited[now] = True

        now = (curr - 1) % 10000
        if not visited[now]:
            Q.append((now, msg + 'S'))
            visited[now] = True

        now = TurnLeft(curr)
        if not visited[now]:
            Q.append((now, msg + 'L'))
            visited[now] = True

        now = TurnRight(curr)
        if not visited[now]:
            Q.append((now, msg + 'R'))
            visited[now] = True
        
for _ in range(int(input())):
    start, target = map(int, input().split())
    print(BFS(start, target))