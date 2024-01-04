A = int(input())
B = int(input())
C = int(input())
answer = str(A * B * C)

for i in range(10):
    print(answer.count(str(i)))