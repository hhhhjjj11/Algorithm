# 정리
"""
- 치즈 주변의 외부 개수를 셀 때 구멍의 0과 외부를 구분해주어야함!!
- 구멍은 외부로 치지 않으니까 세면 안됨

"""


# 풀이
import sys
from collections import deque

N,M = map(int,sys.stdin.readline().strip().split(" "))

graph = [list(map(int,sys.stdin.readline().strip().split(" "))) for _ in range(N)]


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS():
   
    Q = deque()
    Q.append([0,0])
    is_remain = False

    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    
    temp = []

    while Q:
        i_now, j_now = Q.popleft()
        for k in range(4):
            i_next, j_next = i_now + dx[k], j_now + dy[k]
            
            if 0<=i_next<N and 0<=j_next<M and not visited[i_next][j_next]:
                if graph[i_next][j_next] == 0:
                    Q.append([i_next, j_next])
                    visited[i_next][j_next] = 1

                if graph[i_next][j_next] == 1:
                    is_remain = True
                    temp.append([i_next,j_next])
                    # 큐에들어가는 애들은: 외부 -> 따라서 i_next, j_next는 반드시 -> 외부에 연결된 외부이거나 외부에 연결된 치즈.
                    # 따라서 치즈이면 반드시 -> 외부에 연결된 치즈
    
    for i_next, j_next in temp:            
        count = 0
        for p in range(4):
            i_next_adj, j_next_adj = i_next + dx[p], j_next +dy[p]
            if not graph[i_next_adj][j_next_adj] and visited[i_next_adj][j_next_adj] == 1:
                count+=1
            if count >= 2:
                break
        if count >= 2:
            # 녹는 치즈인 경우에만 visited 처리를 해야함
            visited[i_next][j_next] = 1
            graph[i_next][j_next] = "C"

    return is_remain

def Cto0():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == "C":
                graph[i][j] = 0

def solve():
    result = 0
    while True :
        is_remain= BFS()
        result += 1
        if not is_remain:
            break
        Cto0()

    print(result-1)

solve()