def solution(arr1, arr2):
    A, B, C = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0 for _ in range(C)] for _ in range(A)]
    
    for i in range(A):
        for j in range(C):
            s = sum(arr1[i][k] * arr2[k][j] for k in range(B))
            answer[i][j] = s
                
    return answer