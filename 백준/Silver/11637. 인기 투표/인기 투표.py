from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    N = int(input())
    candidates = [int(input()) for _ in range(N)]
    Sum = sum(candidates)
    sortedCandidates = sorted([(candidates[i], i) for i in range(N)], reverse=True)
    
    if sortedCandidates[0][0] == sortedCandidates[1][0]:
        print("no winner")
    elif sortedCandidates[0][0] / Sum > 0.5:
        print("majority winner", sortedCandidates[0][1] + 1)
    else:
        print("minority winner", sortedCandidates[0][1] + 1)