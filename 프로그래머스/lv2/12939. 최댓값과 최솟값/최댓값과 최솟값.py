def solution(s):
    lit = sorted(map(int, s.split()))
    return f"{lit[0]} {lit[-1]}"