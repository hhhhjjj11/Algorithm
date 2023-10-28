# 정리
"""
처음 문제 봤을 때는,, 걍 bfs 돌리면 될것같은데
아.. 이게 1000*1000만 돌리면 상관이 없는데
직사각형에 벽이 걸리는지 그안에서 반복문을 또돌려야해서 시간초과가 뜨는구나...

** 누적합을 이용한 범위안의 벽이 있는지 판별하기
1. S[i][j] = (0,0) 부터 (i,j) 까지 벽의 갯수
    -> S를 누적합을 이용하여 완성시키기.
2. 원하는것: (Sr,SC) 부터 (Fr,Fc) 중에 벽이 있는가? 즉 벽의 갯수가 0인가?
    -> 원하는것  = 큰네모 - 가로로긴네모 - 세로로긴네모 + 작은네모
                = S[Fr][Fc] - S[Sr-1][Fc] - S[Fr][Sc-1] + S[Sr-1][Sc-1]


** 다른방법: 일반화 할 수 있는건지 모르겠으나 되는 방법..?                
벽에 걸리는지 체크하는 시간을 줄이는 방법 두번째..?
 -> 직사각형범위 완탐: 최대 1000*1000임
 -> 개선: 벽의갯수 : 최대 1000*1000
 ???? 벽의갯수나 직사각형범위나 최대 10**6이니까 노상관 아님?
 하지만! -> 벽의갯수가 존나많으면 애초에 큐에들어가는 경우가 적어지기때문에 벽의갯수로 체크하는게 시간관리상 유리하다..
 아닌가? 모르겟음
 왜 직사각형 범위안에 들어있는 벽이 있는지 벽들을 기준으로 반복문돌리는것이 각 직사각형 영역들이 1인지 확인하는것보다 더 빠른거지??? 
"""
# 풀이
import sys

N, M = map(int, sys.stdin.readline().strip().split())
g = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().strip().split())

from collections import deque

Q = deque()
Q.append([Sr-1,Sc-1,0])

visited = [[0]*M for _ in range(N)]
visited[Sr-1][Sc-1] =1

dr = [1,-1,0,0]
dc = [0,0,1,-1]

S = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1, M+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + g[i-1][j-1]


while Q:
    r_now, c_now, cnt = Q.popleft()
    if r_now == Fr-1 and c_now == Fc-1:
        print(cnt)
        exit(0)

    for i in range(4):
        r_next, c_next = r_now + dr[i], c_now + dc[i]
        if 0<= r_next<N  and 0<= c_next< M and 0<=r_next+H-1<N and 0<=c_next+W-1<M and  not visited[r_next][c_next] :
            blocked = S[r_next+H][c_next+W] + S[r_next][c_next] - S[r_next+H][c_next] - S[r_next][c_next+W] 

            if not blocked:
                visited[r_next][c_next] = 1
                Q.append([r_next,c_next,cnt+1])

print(-1)