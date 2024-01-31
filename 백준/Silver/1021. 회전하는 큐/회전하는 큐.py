from sys import stdin
input = stdin.readline

from collections import deque

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
q = deque([i for i in range(1, N+1)])

answer = 0
for num in numbers:
    while True:
        if q[0] == num:
            q.popleft()
            break
        else:
            if q.index(num) < len(q) / 2:
                while q[0] != num:
                    q.append(q.popleft())
                    answer += 1
            else:
                while q[0] != num:
                    q.appendleft(q.pop())
                    answer += 1
print(answer)