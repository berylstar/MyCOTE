import sys
input = sys.stdin.readline
    
print(sum(max(int(input()), 40) for i in range(5)) // 5)