# 정리
"""


"""
# 풀이
import sys
sys.setrecursionlimit(10 ** 8)
M, N = map(int, sys.stdin.readline().strip().split())

graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

dp = [[0]*N for _ in range(M)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(i,j):
    # print("==============")
    # for a in dp:
    #     print(a)
    
    for p in range(4):
        i_next, j_next = i + dx[p], j + dy[p]

        if 0<=i_next<M and 0<=j_next<N and graph[i][j] > graph[i_next][j_next]:
            dp[i_next][j_next] +=1
            dfs(i_next,j_next)

dfs(0,0)
dp[0][0]=1
print(dp[M-1][N-1])