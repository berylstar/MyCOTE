from sys import stdin
input = stdin.readline

N = int(input())
tree = {}
for _ in range(N):
    a, b, c = map(str, input().split())
    tree[a] = [b, c]

def PreOrder(start):
    print(start, end='')
    visited.add(start)
    
    left, right = tree[start][0], tree[start][1]
    
    if left != '.' and left not in visited:
        PreOrder(left)
    if right != '.' and right not in visited:
        PreOrder(right)

def InOrder(start):
    left, right = tree[start][0], tree[start][1]
    
    if left != '.' and left not in visited:
        InOrder(left)
        
    print(start, end='')
    visited.add(start)
        
    if right != '.' and right not in visited:
        InOrder(right)

def PostOrder(start):
    left, right = tree[start][0], tree[start][1]
    
    if left != '.' and left not in visited:
        PostOrder(left)
        
    if right != '.' and right not in visited:
        PostOrder(right)

    print(start, end='')
    visited.add(start)

visited = set()
PreOrder('A')
print()
visited.clear()
InOrder('A')
print()
visited.clear()
PostOrder('A')