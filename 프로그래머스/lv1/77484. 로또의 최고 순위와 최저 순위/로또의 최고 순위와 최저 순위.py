def solution(lottos, win_nums):
    a = len(set(lottos) & set(win_nums))
    b = lottos.count(0)
    
    return [min(7 - a - b, 6), min(7 - a, 6)]