# 백준 | 골드5 | 7569 | 토마토

# 기억할것
"""
1. bfs 걸린 시간 세는 방법 
    ->그래프에 기록 할 수 있다. 0인지 아닌지만 중요 (마지막에 -1 해주기)
    - 진원지 + 1 (진원지보다 하루 더 걸림)
2. 그래프와 큐 분리, 큐에는 좌표만. 
    - 그래프와 큐 분리. 
    - 그래프에는 걸린 시간 기록 + 큐에는 안익은 토마토 좌표
"""

# 풀이
import sys
from collections import deque

m,n,h = map(int,input().split())
graph = []
Q = deque([])

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if(temp[j][k]==1):
                Q.append([i,j,k])
    graph.append(temp)

di=[1,-1,0,0,0,0]   
dj=[0,0,1,-1,0,0]   
dk=[0,0,0,0,1,-1]   

while Q:
    i,j,k= Q.popleft()
    for p1 in range(6):
        ni = i+di[p1]
        nj = j+dj[p1]
        nk = k+dk[p1]
        if 0<=ni<h and 0<=nj<n and 0<=nk<m and graph[ni][nj][nk]==0:
            Q.append([ni,nj,nk])
            graph[ni][nj][nk] = graph[i][j][k] + 1

day = 0

for box in graph:
    for row in box:
        for value in row:
            if value ==0:
                print(-1)
                exit(0)
        day = max(day, max(row))

print(day-1)