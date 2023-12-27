import sys
input = sys.stdin.readline

for _ in range(int(input())):
    dic = {}
    for _ in range(int(input())):
        s, l = map(str, input().split())
        dic[s] = dic.get(s, 0) + int(l)
    print(max(dic, key=dic.get))