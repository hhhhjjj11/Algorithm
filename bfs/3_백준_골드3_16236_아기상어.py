# 백준 / 골드3 / 16236 / 아기상어 
"""
1. 
"""

# 풀이
import sys
from collections import deque

N = int(input())
graph = [list(map(int,sys.stdin.readline().strip().split(" "))) for _ in range(N)]

fish = []

for row in range(N):
    for col in range(N):
        if graph[row][col] in {1,2,3,4,5,6}:
            fish.append([row,col])
        if graph[row][col] == 9:
            SP = [row,col] # Start Point 아기상어의 시작지점
            graph[row][col] =  0

dx = [1,-1,0,0]
dy = [0,0,-1,1]

time = 0

SS = 2 # Shark Size 
SEC = 0 # shark eating count

while fish:
    
    Q = deque([])
    Q.append(SP)
    
    visited =[[-1]*N for _ in range(N)]
    visited[SP[0]][SP[1]] +=1

    # 1. 어느 물고기가 가장 가까이 있는지 판별 하기 위해 
    # - n개의 물고기에 대해 일일히 bfs를 돌릴 필요가 없다. -> bfs한번 쫙돌리면 끝
    # - 하나하나 먹어가면서 다음 먹이 찾아가기 -> bfs 반복하기..
    
    while Q:
        x_now, y_now  = Q.popleft()
        for i in range(4):
            x, y = x_now + dx[i], y_now + dy[i]
            if 0<=x<N and 0<=y<N and visited[x][y] == -1 and graph[x][y] <= SS:
                Q.append([x,y])
                visited[x][y] = visited[x_now][y_now] + 1
    
    # 이렇게 하면 visited에 해당 지점까지 가는데 걸린 시간이 표시됨 -> 거리한 칸당 1초이므로 같은 값.
    
    min = 400
    
        # 물고기 중에서 아기상어보다 크기가 작은 애 중에서 가장 가까운애 -> visited에 표시된 값이 가장 작은 애
        # 만약에 visited에 표시된 값이 가장 작은애가 여럿 있으면 맨위부터, 맨위에 여러있으면 왼쪽부터
    fish_x, fish_y = -1,-1
    for x in range(N):
        for y in range(N):
            if [x,y] in fish and 0 < visited[x][y]< min and graph[x][y] < SS: # 0 < visited[x][y] 해줘야함..  그렇지 않으면 지나간적이 없는 물고기에 대해서도 따지게 됨.
                min = visited[x][y]
                fish_x, fish_y = x,y
    
    if fish_x == -1:  
        break
    
    fish.remove([fish_x,fish_y])
    SEC += 1
    if SEC == SS :
        SS += 1
        SEC = 0
    
    SP = [fish_x, fish_y]
    time += visited[fish_x][fish_y]

print(time)