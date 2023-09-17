import sys
input = sys.stdin.readline

from collections import deque
q = deque()

for _ in range(int(input())):
    i = input().rstrip()
    
    if i.startswith("push"):
        q.append(int(i[5:]))
        
    elif i == "size":
        print(len(q))
        
    elif i == "empty":
        print(int(len(q)==0))
        
    elif not q:
        print(-1)
        
    elif i == "pop":
        print(q.popleft())
        
    elif i == "front":
        print(q[0])
            
    elif i == "back":
        print(q[-1])