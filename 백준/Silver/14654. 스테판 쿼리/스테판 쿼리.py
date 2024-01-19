from sys import stdin
input = stdin.readline

N = int(input())

ATeam = list(map(int, input().split()))
BTeam = list(map(int, input().split()))

answer = set()
AWin = 0
BWin = 0

def CheckWin(me, opp):
    return (me==1 and opp==3) or (me==2 and opp==1) or (me==3 and opp==2)

for A, B in zip(ATeam, BTeam):
    if (A == B and BWin > 0) or CheckWin(A, B):
        AWin += 1
        answer.add(BWin)
        BWin = 0
    else:
        BWin += 1
        answer.add(AWin)
        AWin = 0

answer.add(AWin)
answer.add(BWin)
    
print(max(answer))