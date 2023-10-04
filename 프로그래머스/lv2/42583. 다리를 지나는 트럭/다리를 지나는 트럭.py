from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    on = 0

    q = deque()
    trucks = deque(truck_weights)
    
    while trucks or q:
        time += 1
        
        if q and q[0][1] + bridge_length == time:
            on -= q.popleft()[0]
        
        if trucks and on + trucks[0] <= weight:
            t = trucks.popleft()
            q.append([t, time])
            on += t

    return time