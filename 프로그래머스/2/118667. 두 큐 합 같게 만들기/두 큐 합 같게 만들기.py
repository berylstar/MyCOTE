from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    sum1 = sum(q1)
    
    q2 = deque(queue2)
    sum2 = sum(q2)
    
    answer = 0
    
    for _ in range(len(q1)*2 + len(q2)*2):
        if q1 and sum1 > sum2:
            n = q1.popleft()
            sum1 -= n
            
            q2.append(n)
            sum2 += n
        elif q2 and sum1 < sum2:
            n = q2.popleft()
            sum2 -= n
            
            q1.append(n)
            sum1 += n
        elif sum1 == sum2:
            return answer
            break
            
        answer += 1
            
    else:
        return -1