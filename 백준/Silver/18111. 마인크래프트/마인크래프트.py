import math
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]
answer = math.inf
ground = 0

for height in range(257):
    use = 0
    remain = 0
    for i in range(N):
        for j in range(M):
            if blocks[i][j] > height:
                remain += blocks[i][j] - height
            else:
                use += height - blocks[i][j]
    
    if use > remain + B:
        break

    curr = remain * 2 + use

    if curr <= answer:
        answer = curr
        ground = height

print(answer, ground)