def solution(s):
    changeCount = 0
    zeroCount = 0
    
    while s != "1":
        zeroCount += s.count('0')
        
        s = bin(len(s.replace('0', '')))[2:]
        
        changeCount += 1
        
    return [changeCount, zeroCount]