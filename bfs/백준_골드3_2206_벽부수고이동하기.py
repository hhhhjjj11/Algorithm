# 백준 / 골드3 / 2206 / 벽부수고 이동하기


# 풀이
import sys
from collections import deque

N, M = map(int,input().split())

graph = []
check = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
    check.append([0]*M)

Q = deque([])
Q.append([0,0])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while Q:
    Cx, Cy = Q.popleft()
    for i in range(4):
        Nx = Cx + dx[i]
        Ny = Cy + dy[i]

        if 0<=Nx<M and 0<=Ny<N and graph[Nx][Ny]==0 and :
