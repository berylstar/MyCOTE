import sys
input = sys.stdin.readline
import heapq

N = int(input())

q = []

for _ in range(N):
    num = int(input())

    if num == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))

    else:
        heapq.heappush(q, num)