from sys import stdin
input = stdin.readline

N, L, W, H = map(int, input().split())
left, right = 0, max(L, W, H)

for _ in range(10000):
    mid = (left + right) / 2

    if (L // mid) * (W // mid) * (H // mid) >= N:
        left = mid
    else:
        right = mid

print("%.10f" %(right))