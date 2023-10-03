# 정리
"""
혹시 나 천재..?

"""

# 풀이
import sys
from collections import deque

N = int(input())

graph = [list(map(int,sys.stdin.readline().strip().split(" "))) for _ in range(N)]
visited =[[0]*N for _ in range(N)]

land_num = 0

di = [1,-1,0,0]
dj = [0,0,1,-1]

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            land_num += 1
            visited[i][j] = land_num 
            Q = deque()
            Q.append([i,j])

            while Q:
                i_now, j_now = Q.popleft()
                for k in range(4):
                    i_next, j_next = i_now + di[k], j_now + dj[k]
                    if 0<=i_next<N and 0<=j_next<N and not visited[i_next][j_next] and graph[i_next][j_next]==1:
                        visited[i_next][j_next] = land_num
                        Q.append([i_next,j_next])

check = [[0]*N for _ in range(N)]
result = 999

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            needCheck = False
            for k in range(4):
                i_adj, j_adj = i+di[k], j+dj[k]
                if 0<=i_adj<N and 0<=j_adj<N and graph[i_adj][j_adj] == 0:
                    # i,j가 바다랑 인접한 육지라는 뜻이므로. 탐색 대상임.
                    needCheck=True
                    break
            if needCheck:
                check[i][j] = 1
                land_num_now = visited[i][j]
                Q = deque()
                Q.append([i,j])
                visited2 = [[0]*N for _ in range(N)]
                while Q:
                    i_now, j_now = Q.popleft()
                    for p in range(4):
                        i_next, j_next = i_now + di[p], j_now + dj[p]
                        if 0<=i_next<N and 0<=j_next<N and not visited2[i_next][j_next]:
                            if graph[i_next][j_next] == 0:
                                Q.append([i_next,j_next])
                                visited2[i_next][j_next] = visited2[i_now][j_now]+1
                            elif graph[i_next][j_next] == 1 and visited[i_next][j_next] != land_num_now: # 다른 섬에 당도했으면
                                if result > visited2[i_now][j_now]:
                                    result = visited2[i_now][j_now]

print(result)