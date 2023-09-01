# 1월 1일은 금요일
def solution(a, b):
    return ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"][(sum([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:a-1]) + b + 4) % 7]