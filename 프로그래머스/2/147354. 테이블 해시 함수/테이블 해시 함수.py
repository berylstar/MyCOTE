from functools import reduce
def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1], -x[0]))
    
    # s = []
    # for i in range(row_begin, row_end+1):
    #     s.append(sum(n%i for n in data[i-1]))
    
    s = [sum(n%i for n in data[i-1]) for i in range(row_begin, row_end + 1)]
        
    answer = s[0]
    for n in s[1:]:
        answer = answer ^ n
    return answer