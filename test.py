def solution(m, n, puddles):
    dp = [[1]*m for _i in range(n)]
    for k in range(len(puddles)):
        dp[puddles[k][1]-1][puddles[k][0]-1] = 0

    for i in range(1,n):
        for j in range(1,m):
            if i*j != 0:
                if dp[i][j] != 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    answer = dp[n-1][m-1]
    print(dp)
    return answer%1000000007



print(solution(4,3,[[2,2]]))

print(solution(5,4,[[2,2]]))