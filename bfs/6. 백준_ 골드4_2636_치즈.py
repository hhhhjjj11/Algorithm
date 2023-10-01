# 정리
"""
1. 우선 뭐 효율을 위해서 edge만 따로 체크할 필요가 없다. 어차피 novisited 조건 걸면 차이 안난다.
- 괜히 복잡해지기만 하고 출제 의도에서 벗어나는 듯 하다.
2. visited 조건 활용 -> 더이상 탐색 X

"""

# 풀이
import sys
from collections import deque

H,W = map(int,sys.stdin.readline().strip().split(" "))

graph = [list(map(int,sys.stdin.readline().strip().split(" "))) for _ in range(H)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS():
    Q = deque([])
    Q.append([0,0])

    visited = [[0]*W for _ in range(H)]
    visited[0][0] = 1

    while Q:
        x_now, y_now = Q.popleft()
        for i in range(4):
            x_next, y_next = x_now + dx[i] , y_now + dy[i]
            if 0<=x_next<H and 0<=y_next<W and not visited[x_next][y_next]:
                if graph[x_next][y_next] == 0:
                    visited[x_next][y_next] = 1
                    Q.append([x_next,y_next])
                    
                elif graph[x_next][y_next] == 1:
                    graph[x_next][y_next] = 0 
                    visited[x_next][y_next] =1 

def remain():
    cheeze = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1:
                cheeze += 1
    return cheeze

def Solution():
    hours = 0
    cheeze_remain = remain()
    if not cheeze_remain:
        print(0)
        print(0)
        exit(0)

    while True:
        BFS()
        hours += 1

        if not remain():
            break
        
        cheeze_remain = remain()

    print(hours)
    print(cheeze_remain)
    
Solution()