# 백준 / 골드3 / 2206 / 벽부수고 이동하기

# 풀이 
import sys
from collections import deque

N,M = map(int,sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

visited = [[[0,0]* M] for _ in range(N)]

Q = deque([])
Q.append([0,0,0])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

while Q:
    
    Cx, Cy, isbroke = Q.popleft()
    
    for i in range(4):
        Nx = Cx + dx[i]
        Ny = Cy + dy[i]

        if 0<=Nx<N and 0<=Nx<M:
            if isbroke == 0:  # 만약에 벽을 뚫은 적이 없는 상태라면
                pass
                if visited[Nx][Ny][0]
            else: # 벽을 뚫은 경우
