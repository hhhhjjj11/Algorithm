# 정리
"""
시간초과 -> 계산 할 필요 없는 경우는 계산 안하도록 걸러줘야함!!
이 문제의 경우에는 연합의 국가가 1개인 경우는 계산을 하지 않도록 해줘야 시간초과가 안난다.

"""

# 풀이
import sys
from collections import deque


N,L,R = map(int,sys.stdin.readline().strip().split(" "))
graph = [list(map(int,sys.stdin.readline().strip().split(" "))) for _ in range(N)]

MoveOrNot = True # 인구 이동을 할지 말지 (국경선 열었는지 여부)
# 인구 이동을 할지 말지는 국경선열뿐만아니라, 연합내의 인구가 모두 같지 않아야함. 한군데라도 다른 땅이 있어야 이동이 일어남.

dx = [1,-1,0,0]
dy = [0,0,1,-1]

count = 0

while MoveOrNot: # 인

    MoveOrNot = False
    check = [[0]*N for _ in range(N)]
    union_number = 1 # 연합을 구분하기 위해 설정
    
    record_value = []

    for i in range(N):
        for j in range(N):
            if not check[i][j]:
                check[i][j] = union_number
                Q = deque([])
                Q.append([i,j])

                temp = graph[i][j]
                cnt = 1

                while Q:
                    x_now, y_now = Q.popleft()

                    for k in range(4):
                        x_next , y_next = x_now + dx[k] , y_now + dy[k]

                        if 0<=x_next<N and 0<=y_next<N and not check[x_next][y_next]:
                            sub = abs(graph[x_next][y_next] - graph[x_now][y_now])
                            if L<=sub<=R:
                                Q.append([x_next,y_next])
                                temp += graph[x_next][y_next]
                                cnt += 1
                                check[x_next][y_next] = union_number
                                if sub>0:
                                    MoveOrNot = True # 국경선 열고 + sub>0 일 경우 인구이동 필요함.
                if cnt >1 : 
                    record_value.append(temp//cnt)
                else:
                    record_value.append(-1)
                union_number += 1
    
    if MoveOrNot:
        for i in range(1, union_number):
            if record_value[i-1]>0:
                for x in range(N):
                    for y in range(N):
                        if check[x][y] == i:
                            graph[x][y] = record_value[i-1]
                     
        count += 1

print(count)