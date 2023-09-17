import sys
input = sys.stdin.readline

from collections import deque
q = deque()

for _ in range(int(input())):
    i = input().rstrip()
    
    if i.startswith("push"):
        q.append(int(i[5:]))
    elif i == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif i == "size":
        print(len(q))
    elif i == "empty":
        print(int(len(q)==0))
    elif i == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif i == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])