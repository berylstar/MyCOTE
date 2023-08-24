import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

numDict = { v:i for i, v in enumerate(sorted(set(arr)))}
    
print(*[numDict[i] for i in arr], sep=" ")