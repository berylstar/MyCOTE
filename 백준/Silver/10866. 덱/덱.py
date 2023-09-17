import sys
input = sys.stdin.readline

from collections import deque
q = deque()

for _ in range(int(input())):
    i = input().rstrip()
    
    if i.startswith("push_back"):
        q.append(int(i[10:]))
        
    elif i.startswith("push_front"):
        q.appendleft(int(i[11:]))
        
    elif i == "size":
        print(len(q))
        
    elif i == "empty":
        print(int(len(q)==0))
        
    elif not q:
        print(-1)
        
    elif i == "pop_front":
        print(q.popleft())
    
    elif i == "pop_back":
        print(q.pop())
        
    elif i == "front":
        print(q[0])
            
    elif i == "back":
        print(q[-1])