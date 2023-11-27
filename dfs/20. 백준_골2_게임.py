# 정리
"""
bottom up 으로 해야 시간초과 안나는듯.
"""
# 풀이
import sys

N, M = map(int, sys.stdin.readline().strip().split())

board = [list(sys.stdin.readline().strip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] != 'H':
            board[i][j] = int(board[i][j])

di = [0,0,1,-1]
dj = [1,-1,0,0]

visited= [[0]*M for _ in range(N)]
MAX = 0
def DFS(i,j, cnt):
    global MAX

    if cnt > MAX:
        MAX = cnt

    V = board[i][j]
    for p in range(4): 
        i_next, j_next =i + V*di[p], j + V*dj[p]
        if 0<=i_next<N and 0<=j_next<M and visited[i_next][j_next]:
            print(-1)
            exit(0)
        if 0<=i_next<N and 0<=j_next<M and not visited[i_next][j_next] and board[i_next][j_next] != 'H':
            visited[i_next][j_next] = 1
            DFS(i_next,j_next, cnt+1)
            visited[i_next][j_next] = 0

visited[0][0] =1
DFS(0,0,0)
print(MAX+1)