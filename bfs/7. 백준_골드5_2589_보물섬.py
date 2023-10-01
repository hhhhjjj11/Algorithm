# 정리
"""
1. 모든 지점에서 bfs를 돌리는게 맞아? 라고 의심했지만 그게 맞았다
- 골드 5따리라 그냥 갈기면 되나보다
"""
# 풀이
import sys
from collections import deque

r, c = map(int,sys.stdin.readline().strip().split(" "))

graph = [list(sys.stdin.readline().strip()) for _ in range(r)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i,j):
    visited = [[0]*c for _ in range(r)]
    visited[i][j] = 1 
    Q = deque()
    Q.append([i,j])

    while Q:
        x_now , y_now = Q.popleft()
        for k in range(4):
            x_next, y_next = x_now + dx[k], y_now + dy[k]
            if 0<=x_next<r and 0<=y_next<c and not visited[x_next][y_next] and graph[x_next][y_next] == "L":
                Q.append([x_next,y_next])
                visited[x_next][y_next] = visited[x_now][y_now] + 1

    res = 0 
    for i in range(r):
        for j in range(c):
            if visited[i][j] > res:
                res = visited[i][j]
    return res

def sol():
    max = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] =="L":
                if max < bfs(i,j):
                    max = bfs(i,j)

    print(max-1)

sol()