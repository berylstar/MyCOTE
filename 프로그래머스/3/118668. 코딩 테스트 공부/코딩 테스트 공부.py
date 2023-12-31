def solution(alp, cop, problems):
    max_alp = max(problems, key=lambda i:i[0])[0]
    max_cop = max(problems, key=lambda i:i[1])[1]
        
    max_alp = max(0, max_alp - alp)
    max_cop = max(0, max_cop - cop)
    
    dp = [[i + j for i in range(max_cop + 1)] for j in range(max_alp + 1)]
    dp[0][0] = 0
    
    for i in range(max_alp + 1):
        for j in range(max_cop + 1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req - alp and j >= cop_req - cop:
                    next_alp = min(max_alp, i + alp_rwd)
                    next_cop = min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)

    return dp[max_alp][max_cop]