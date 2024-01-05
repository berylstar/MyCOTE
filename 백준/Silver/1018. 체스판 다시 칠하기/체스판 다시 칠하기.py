import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

answer = set()

for i in range(N - 7):
    for j in range(M - 7):
        w_index = 0
        b_index = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        w_index += 1
                    else:
                        b_index += 1
                else:
                    if board[a][b] != 'W':
                        b_index += 1
                    else:
                        w_index += 1
        answer.add(w_index)
        answer.add(b_index)
print(min(answer))