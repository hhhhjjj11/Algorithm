# 정리
"""
아주 좋은 문제 같다.

BFS + DX + 다차원(스킬쓸때안쓸때)


"""

# 풀이
import sys
from collections import deque

K = int(input())
W, H = map(int,input().split())

if W==H==1:
    print(0)
    exit(0)
graph = [list(map(int,sys.stdin.readline().strip().split(" "))) for _ in range(H)]

visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
visited[0][0][0] = 1
horse =[(-2,1),(-1,2),(1,2),(2,1),(-1,-2),(-2,-1),(1,-2),(2,-1)] # len : 8
monkey = [(1,0),(-1,0),(0,1),(0,-1)]

deck = deque()
deck.append([0,0,0]) # i,j,K

DX = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
DX[0][0][0] = 0

while deck:
    i_now, j_now, use = deck.popleft()
    
    if use<K: # 아직 말처럼 이동 가능 함
        for di,dj in horse:
            i_next, j_next = i_now + di , j_now + dj
            if 0<=i_next<H and 0<=j_next<W and not graph[i_next][j_next]:
                if not visited[i_next][j_next][use+1]:
                    deck.appendleft([i_next,j_next,use+1])
                    DX[i_next][j_next][use+1] = DX[i_now][j_now][use] + 1
                    visited[i_next][j_next][use+1] = 1
                else:
                    # 가중치의 역전이 일어날 수 있는 부분에 대해서는 visited하였더라도 DX의 대소를 체크 해줘야함
                    if DX[i_now][j_now][use] + 1 < DX[i_next][j_next][use+1]:
                        DX[i_next][j_next][use+1] = DX[i_now][j_now][use] + 1
    
    for di,dj in monkey:
        i_next, j_next = i_now + di , j_now + dj
        if 0<=i_next<H and 0<=j_next<W and not visited[i_next][j_next][use] and not graph[i_next][j_next]:
            deck.append([i_next, j_next, use])
            DX[i_next][j_next][use] = DX[i_now][j_now][use] + 1
            visited[i_next][j_next][use] = 1
        
min = 100000
for value in DX[H-1][W-1]:
    if value>0 and min>value:
        min = value

if min == 100000:
    min = -1

print(min)