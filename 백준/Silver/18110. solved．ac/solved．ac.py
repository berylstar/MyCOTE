import sys
input = sys.stdin.readline

def ROUND(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)
 
T = int(input())

difs = [int(input()) for _ in range(T)]
cut = ROUND(T * 0.15)

if T == 0:
    print(0)
else:
    if cut > 0:
        difs = sorted(difs)[cut:T - cut]
    print(ROUND(sum(difs) / len(difs)))