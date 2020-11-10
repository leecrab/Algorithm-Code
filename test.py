# 프로그래머스 멀리뛰기

def solution(n):
    answer = 0
    dp = [0 for i in range(n)]
    dp[0] = 1
    dp[1] = 2
    for i in range(2,n):
        dp[i] = (dp[i-1] +dp[i-2])
    return dp[n-1]
