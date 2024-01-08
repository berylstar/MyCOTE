from collections import deque
import math

positions = [math.inf for _ in range(100001)]

N, K = map(int, input().split())

q = deque()
q.append((N, 0))

while q:
    currPos, currCnt = q.popleft()

    if currPos < 0 or currPos > 100000:
        continue

    if positions[currPos] <= currCnt:
        continue

    positions[currPos] = currCnt

    if currPos == K:
        continue

    q.append((currPos + 1, currCnt + 1))
    q.append((currPos - 1, currCnt + 1))
    q.append((currPos * 2, currCnt + 1))

print(positions[K])