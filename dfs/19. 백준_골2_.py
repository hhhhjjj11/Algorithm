# 정리
"""
dp 없는 dfs쓰면 시초 나는 이유 : 
(원래 dfs 시간복잡도가 O(V+E), O(V^2) 라고 흔히 하지만 그건 특정한 데이터 타입의 경우고 여기서는
4**n 이 맞는듯.)
시간복잡도 4*4*4*4*... 가 가능한데
크기가 50 50 이면 입력에 따라 4**15승 이상도 충분히 가능하고
4**15만 돼도 10억이 넘어감
"""

# 풀이
import sys

N, M = map(int,sys.stdin.readline().strip().split())

board = [list(sys.stdin.readline().strip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'H':
            continue
        board[i][j] = int(board[i][j])

# dfs(i,j) = i,j에서 최대로 움직일 수 있는 횟수
dp = [[0]*M for _ in range(N)]

di = [0,0,1,-1]
dj = [1,-1,0,0]

visited = [[0]*M for _ in range(N)]
visited[0][0] = 1

def dfs(i,j):

    if dp[i][j]:
        return dp[i][j]
    
    v_now = board[i][j]

    for k in range(4):
        i_next, j_next = i + v_now*di[k] , j + v_now*dj[k]
        if 0<=i_next<N and 0<=j_next<M and board[i_next][j_next] != 'H':
            if visited[i_next][j_next]:
                print(-1)
                exit(0)
            if not visited[i_next][j_next]:
                visited[i_next][j_next] = 1
                NEXT = dfs(i_next,j_next)
                if NEXT + 1 > dp[i][j]:
                    dp[i][j] = NEXT + 1
                visited[i_next][j_next] = 0
                
    return dp[i][j]

print(dfs(0,0)+1)