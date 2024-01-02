from collections import deque
N = int(input())

sett = set()
sett.add(N)
q = deque()
q.append((N, 0))

answer = set()

while q:
    num, count = q.popleft()
    
    if num == 1:
        answer.add(count)
        break
    
    if num % 3 == 0 and num // 3 not in sett:
        sett.add(num // 3)
        q.append((num // 3, count + 1))
    if num % 2 == 0 and num // 2 not in sett:
        sett.add(num // 2)
        q.append((num // 2, count + 1))
    if num - 1 not in sett:
        sett.add(num - 1)
        q.append((num - 1, count + 1))
print(min(answer))