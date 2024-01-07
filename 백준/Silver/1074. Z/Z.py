N, r, c = map(int, input().split())
answer = 0

for _ in range(N):
    N -= 1
    eff = 2 ** N

    if r < eff:
        if c < eff:
            quadrant = 0
        else:
            quadrant = 1
            c -= eff
    else:
        if c < eff:
            quadrant = 2
        else:
            quadrant = 3
            c -= eff
    
        r -= eff

    answer += eff * eff * quadrant
print(answer)