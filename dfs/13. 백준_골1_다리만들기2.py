# 정리
"""

"""
# 풀이
import sys
import heapq
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
g = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

"""
섬: 노드
섬과 섬사이의 길 중에서 최소 : 간선
  - 대각선에 위치하면 세로쭉 가로쭉으로는 연결이 안될 수도 있음
그걸 기반으로 mst구하면 됨.

순서 1. 섬구분
2. 섬과 섬 사이에 간선길이(가중치) 구하기
3. mst
"""
visited = [[0]*M for _ in range(N)]

di = [0,0,1,-1]
dj = [1,-1,0,0]

def dfs(i,j):
    global flag
    
    visited[i][j] = flag

    for k in range(4):
        i_next, j_next = i + di[k] , j + dj[k]
        if 0<=i_next< N and 0<=j_next< M and not visited[i_next][j_next] and g[i_next][j_next] == 1:
            dfs(i_next,j_next)

flag = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and g[i][j] == 1:
            flag += 1
            dfs(i,j)

# for row in visited:
#     print(row)
    
def bridge(i,j, di,dj):
    # print('sdfsdfsdfsf')
    i_next, j_next = i + di, j + dj
    # 범위 안에 있고 바다일 경우
    if 0<= i_next< N and 0<=j_next <M and not g[i_next][j_next]:
        # 다리 건설 시작
        length = 1
        # print('i,j', i, j)
        # print('다리건설시작')
        while True:
            # print('다음좌표', i_next,j_next)
            i_next += di
            j_next += dj
            if not (0<=i_next<N and 0<=j_next<M):
                return 0
            
            if g[i_next][j_next]: # 다음 칸이 육지일경우
                if visited[i_next][j_next] != visited[i][j]:    # 다음 칸이 다른 지역의 땅일 경우
                    if length ==1:
                        return 0
                    else:
                        return length, visited[i_next][j_next]
                else:
                    return 0
            length += 1

    return 0

g2 = {}

for i in range(N):
    for j in range(M):
        # 바다와 인접한 육지에 대해서만 bridge 함수 실행
        if not g[i][j]: # 바다라면 넘어감
            continue
        s = visited[i][j]

        for x in range(4):
            res = bridge(i,j,di[x],dj[x])
            if not res:
                continue
            # 만약에 다리가 있으면....?
            br, e = res     # 다리길이, 도착 육지번호
            if s in g2:
                g2[s].append([br,e])
                pass
            else:
                g2[s] = [[br,e]]
            if e in g2:
                g2[e].append([br,s])
            else:
                g2[e] = [[br,s]]

# print(g2)
            
# 여기 까지 하면 g2안에 중복된 간선들이 있는데. 중복 상관 없긴하지않나??

heap=[[0,1]]

visitednode = set()

cnt = 0
ans = 0

check = [0]*(flag+1)
MS = set()
MS.add(1)
Q = deque([1])

if len(g2) != flag:
    print(-1)
    exit(0)

while Q:
    now = Q.popleft()
    check[now] = 1
    for li in g2[now]:
        # print('i', li)
        weight, adj = li
        if not check[adj]:
            MS.add(adj)
            Q.append(adj)
            
if len(MS) != flag:
    print(-1)
    exit(0)

while heap:
    weight, node = heapq.heappop(heap)
    
    if node in visitednode:
        continue

    cnt += 1
    ans += weight

    if cnt == flag:
        break

    visitednode.add(node)
    for i in g2[node]:
        heapq.heappush(heap,i)

print(ans)