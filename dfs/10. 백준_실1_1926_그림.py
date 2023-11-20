import sys
from collections import deque

n, m = map(int,sys.stdin.readline().strip().split())
g = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

di = [1,-1,0,0]
dj = [0,0,-1,1]

visited = [[0]*m for _ in range(n)]

def dfs(i,j, cnt):
    for k in range(4):
        i_next, j_next = i+di[k], j+dj[k]
        
        if 0<=i_next<n and 0<=j_next<m and not visited[i_next][j_next]:
            visited[i_next][j_next] = 1
            dfs(i_next, j_next, cnt+1)
            visited[i_next][j_next] = 0



# bfs 풀이가 먼저 생각나서 bfs풀어서 바로 맞. dfs로 해보자.
# Q = deque()
# flag = 0
# for i in range(n):
#     for j in range(m):
#         if not visited[i][j] and g[i][j] == 1:
#             flag += 1
#             Q.append((i,j))
#             visited[i][j] = flag
#             while Q:
#                 i_now, j_now = Q.popleft()
#                 for p in range(4):
#                     i_next, j_next = i_now + di[p], j_now + dj[p]
#                     if 0<=i_next<n and 0<=j_next < m and not visited[i_next][j_next] and g[i_next][j_next]==1:
#                         Q.append((i_next,j_next))
#                         visited[i_next][j_next] = flag

# M = 0
# result = [0]*(flag+1)
# for i in range(n):
#     for j in range(m):
#         if visited[i][j]:
#             result[visited[i][j]] += 1
# print(flag)
# print(max(result))