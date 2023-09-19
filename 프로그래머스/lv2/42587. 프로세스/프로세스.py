def solution(priorities, location):
    answer = 1
    while True:
        M = max(priorities)
        for i in range(len(priorities)):
            if priorities[i] == M:
                if i == location:
                    return answer
                priorities[i] = 0
                answer += 1
                M = max(priorities)