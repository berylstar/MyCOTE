from sys import stdin
input = stdin.readline

N = int(input())
students = [list(map(int, input().split())) for _ in range(N)]

schoolDict = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}}
for student, info in enumerate(students, start=1):
    for grade, ban in enumerate(info, start=1):
        schoolDict[grade][ban] = schoolDict[grade].get(ban, []) + [student]

cost = [[] for _ in range(N+1)]

for grade in schoolDict.keys():
    for ban in schoolDict[grade]:
        if len(schoolDict[grade][ban]) > 1:
            for student in schoolDict[grade][ban]:
                cost[student].extend(schoolDict[grade][ban])

answer = 1
temp = 0
for i in range(N+1):
    if temp < len(set(cost[i])):
        answer = i
        temp = len(set(cost[i]))
print(answer)