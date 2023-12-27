import sys
input = sys.stdin.readline

for _ in range(int(input())):
    mars = list(map(str, input().split()))
    answer = float(mars[0])
    for i in range(1, len(mars)):
        if mars[i] == "#":
            answer -= 7
        elif mars[i] == "%":
            answer += 5
        elif mars[i] == "@":
            answer *= 3
                
    print(f"{answer:.2f}")