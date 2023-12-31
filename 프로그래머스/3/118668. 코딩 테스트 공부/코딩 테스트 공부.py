import math
def solution(alp, cop, problems):
    max_alp = max(problems, key=lambda i:i[0])[0]
    max_cop = max(problems, key=lambda i:i[1])[1]
        
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    dp = [[math.inf for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
                
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, time in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp,next_cop = min(max_alp,i + alp_rwd), min(max_cop,j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop],dp[i][j] + time)

    return dp[max_alp][max_cop]