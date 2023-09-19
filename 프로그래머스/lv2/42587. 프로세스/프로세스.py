def solution(priorities, location):
    ans = 1
    while True:
        M = max(priorities)
        for i in range(len(priorities)):
            if priorities[i] == M:
                if i == location:
                    return ans
                priorities[i] = 0
                ans += 1
                M = max(priorities)