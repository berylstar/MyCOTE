N, r, c = map(int, input().split())
answer = 0

while N != 0:
    N -= 1
    eff = 2 ** N
    quadrant = 0
    
    if r >= eff:
        quadrant += 2
        r -= eff
    
    if c >= eff:
        quadrant += 1
        c -= eff

    answer += eff * eff * quadrant
    
print(answer)