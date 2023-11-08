# 정리
"""
dfs + dp 같은데
bottom up 으로 해결함
top down으로도 풀어보자..

bottom up 으로 경로의 수 풀기
1. dp[i][j] = (i,j)에서 목적지까지의 경로의 수 
2. 재귀를 통해서, 가장 끝단부터 후처리되어 누적됨
3. 방문처리등도 까다로운 요소임. 잘 정리하기
"""
# 풀이
import sys

N = int(input())
g = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[-1]*N for _ in range(N)]  # dp[A][B] : A,B에서 도착점까지 가는 경우의 수

di = [0,1]
dj = [1,0]

def dfs(i,j):
    if i == N-1 and j == N-1:
        return 1
    if dp[i][j] > -1:
        return dp[i][j]
    
    dp[i][j] = 0

    for p in range(2):
        k = g[i][j] 
        if k == 0:
            continue
        # if 0<=i+di[p]*k < N and 0<=j+dj[p]*k < N and dp[i+di[p]*k][j+dj[p]*k]==-1:
        if 0<=i+di[p]*k < N and 0<=j+dj[p]*k < N :
            dp[i][j] += dfs(i+di[p]*k, j+dj[p]*k)
            # print(i,j,'/', dp[i][j])
    return dp[i][j]

dfs(0,0)
# for row in dp:
#     print(row)

print(dp[0][0])