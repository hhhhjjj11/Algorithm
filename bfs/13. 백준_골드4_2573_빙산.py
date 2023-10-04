# 정리

# 풀이
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split(" "))

graph = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def after1year():
    record = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j]: # 0 이 아니면
                count = 0
                for k in range(4):
                    i_adj , j_adj = i + dx[k] , j + dy[k]
                    if 0 <= i_adj < N and 0 <= j_adj < M and graph[i_adj][j_adj] == 0:
                       count +=1
                record[i][j]=count

    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                graph[i][j] = max(0, graph[i][j] - record[i][j])

def check():
    
    landnum = 0
    visited = [[-1]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if graph[i][j] and visited[i][j]== -1 : # 0 이 아니면 bfs 시작 
                Q= deque()
                Q.append([i,j])
                visited[i][j] = landnum
                while Q:
                    i_now , j_now = Q.popleft()
                    for p in range(4):
                        i_next, j_next = i_now + dx[p], j_now +dy[p]
                        
                        if 0<=i_next<N and 0<=j_next <M and visited[i_next][j_next] == -1 and graph[i_next][j_next]:
                            visited[i_next][j_next] = landnum
                            Q.append([i_next,j_next])
                landnum+=1
    return landnum

def solve():

    res = 0
    if check() > 1:
        print(0)
        return
    
    while True:
        after1year()
        res+=1
        if check() > 1:
            break
    
    print(res)
    return

solve()