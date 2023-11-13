# 정리
"""
bottom up 으로
완탐돌리면 당연 시간초과
"""
# 풀이
import sys

n = int(input())

g = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

di = [1,-1,0,0]
dj = [0,0,1,-1]

dp = [[0]*n for _ in range(n)] # dp[i][j] = i,j에서 최대값 

def dfs (i,j):

    if dp[i][j]:
        return dp[i][j]

    dp[i][j] = 1 

    for k in range(4):
        i_next, j_next = i + di[k], j + dj[k]

        if 0<=i_next<n and 0<=j_next< n and  g[i_next][j_next] > g[i][j]:
            dp[i][j] = max(dp[i][j], dfs(i_next,j_next)+1)  
    
    return dp[i][j]

answer = 0

for p in range(n):
    for q in range(n):
        answer = max(answer, dfs(p,q))

print(answer)