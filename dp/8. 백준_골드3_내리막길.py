# 정리
"""
아이디어.. 신박하다 (존나 흔한건데 난 첨봣네..)
dfs라고 같은 dfs가 아님. 

모든 노드들을 끝까지 탐색하는 방식으로 하면서 +1씩 세면 시간초과가 난다.
그것이 아니라, 

bottom->up으로 센다..  보통 .. dp문제를 dfs로 풀대 bottom up방식을 쓴다.

"""
# 풀이
import sys
sys.setrecursionlimit(10 ** 8)
M, N = map(int, sys.stdin.readline().strip().split())

graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

dp = [[-1]*N for _ in range(M)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(i,j):
    
    if i==M-1 and j==N-1:
        return 1

    # 가본적이 없는 땅이면
    if dp[i][j] == -1:
        dp[i][j] = 0
    
        for p in range(4):
            i_next, j_next = i + dx[p], j + dy[p]
            
            if 0<=i_next<M and 0<=j_next<N and graph[i][j] > graph[i_next][j_next]:
                dp[i][j] += dfs(i_next,j_next)

    return dp[i][j]

print(dfs(0,0))