from collections import deque
import sys
input = sys.stdin.readline

def Printer(N, M, priorities):
    q = deque(priorities)
    ret = 0
    while q:
        best = max(q)
        front = q.popleft()
        M -= 1
        
        if front == best:
            ret += 1
            if M < 0:
                return ret
        else:
            q.append(front)
            if M < 0:
                M = len(q) - 1
            

for _ in range(int(input())):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    print(Printer(N, M, priorities))