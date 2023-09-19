from collections import Counter
from functools import reduce
def solution(clothes):
    c = Counter([i[1] for i in clothes])
    return reduce(lambda acc,y : acc * (y+1), c.values(), 1) - 1