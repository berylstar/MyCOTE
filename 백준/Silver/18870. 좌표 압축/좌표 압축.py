import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

numDict = {}
for i, v in enumerate(sorted(set(arr))):
    numDict[v] = i
    
lit = [numDict[i] for i in arr]
print(*lit, sep=" ")