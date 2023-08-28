def solution(s):
    return int([s:=s.replace(v, str(i)) for i, v in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])][-1])