def Check(cookie, l, r):
    leng = len(cookie)
    left = cookie[l]
    right = cookie[r]
    
    ret = 0
    
    while 0 <= l and r < leng:
        if left < right:
            if l > 0:
                l -= 1
                left += cookie[l]
            else:
                break
            
        elif left > right:
            if r < leng - 1:
                r += 1
                right += cookie[r]
            else:
                break
            
        elif left == right:
            ret = left
            
            if l > 0:
                l -= 1
                left += cookie[l]
            
            elif r < leng - 1:
                r += 1
                right += cookie[r]
                
            else:
                break
    
    return ret
        
def solution(cookie):
    if len(cookie) < 2:
        return 0
    else:
        return max([Check(cookie, i, i + 1) for i in range(len(cookie) - 1)])