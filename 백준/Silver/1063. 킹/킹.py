from sys import stdin
input = stdin.readline

dir = {'R':[1,0], 'L':[-1,0], 'B':[0,-1], 'T':[0,1],
       'RT':[1,1], 'LT':[-1,1], 'RB':[1,-1], 'LB':[-1,-1]}

king, stone, N = map(str, input().split())

kx, ky = ord(king[0]) - 64, int(king[1])
sx, sy = ord(stone[0]) - 64, int(stone[1])

for _ in range(int(N)):
    d = dir[input().rstrip()]
    
    nkx, nky = kx + d[0], ky + d[1]

    if nkx < 1 or nkx > 8 or nky < 1 or nky > 8:
        continue

    if nkx == sx and nky == sy:
        nsx, nsy = sx + d[0], sy + d[1]

        if nsx < 1 or nsx > 8 or nsy < 1 or nsy > 8:
            continue

        sx, sy = nsx, nsy

    kx, ky = nkx, nky

print(chr(kx + 64), ky, sep='')
print(chr(sx + 64), sy, sep='')