import sys
input = sys.stdin.readline

answer = 0

for i in range(5):
    answer += max(int(input()), 40)
    
print(answer // 5)