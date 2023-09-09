def solution(s):
    lit = sorted(map(int, s.split()))
    return str(lit[0]) + " " + str(lit[-1])