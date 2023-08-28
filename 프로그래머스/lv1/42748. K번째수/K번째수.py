def solution(array, commands):
    return [sorted(array[l-1:r])[i-1] for l, r, i in commands]