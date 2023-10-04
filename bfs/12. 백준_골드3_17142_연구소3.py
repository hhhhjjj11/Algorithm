# 정리
"""
- 조합 섞음. 문제가 복잡하다보니까 아이디어가 신박한건 없는데 로직이 복잡해져서 헷갈리는게 많고 정답내는로직도 복잡함
- 많은 연습을 통해 휙휙 풀 수 있도록 해야할듯.
"""

# 풀이
import sys
from collections import deque

N, M = map(int,sys.stdin.readline().strip().split(" "))

graph = [list(map(int,sys.stdin.readline().strip().split(" "))) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append([i,j])

NOV = len(virus)    # Num of Virus

def combination(n, r):
    def backtrack(start, path):
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(start, n+1):
            path.append(i)
            backtrack(i+1, path)
            path.pop()

    result = []
    backtrack(1,[])
    return result

lists = combination(NOV, M)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

results = []
for list in lists:
    Q = deque()
    visited =[[-1]*N for _ in range(N)]

    for x in range(M):  # M = lent(list) 즉 초기 활성화 시킬 바이러스 개수
        i_v, j_v = virus[list[x]-1]  # list[x] = virus 번호
        graph[i_v][j_v] = 0
        visited[i_v][j_v] = 0
        Q.append([i_v,j_v])
    
    while Q:
        i_now , j_now = Q.popleft()
        
        for k in range(4):
            i_next, j_next = i_now + dx[k], j_now + dy[k]

            if 0<=i_next<N and 0<=j_next<N and visited[i_next][j_next] == -1:
                if graph[i_next][j_next] == 0:
                    visited[i_next][j_next] = visited[i_now][j_now] + 1
                    Q.append([i_next,j_next])
                elif graph[i_next][j_next] == 2:
                    for p in range(4):
                        i_adj, j_adj = i_next + dx[p], j_next +dy[p]
                        if 0<= i_adj <N and 0<= j_adj <N and visited[i_adj][j_adj]==-1 and graph[i_adj][j_adj] == 0:
                            Q.append([i_next,j_next])
                            visited[i_next][j_next] = visited[i_now][j_now]+1
                            break
    
    for i in range(NOV):
        visited[virus[i][0]][virus[i][1]] = 0
    
    possible =True
    time = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 1 and visited[i][j] == -1 :
                results.append(-1)
                possible = False
                break
            if visited[i][j] > time:
                time = visited[i][j]
        if not possible:
            break
    if possible:
        results.append(time)

if max(results) == -1:
    print(-1)
    exit(0)

else:
    ans = 9999
    for r in results:
        if r<ans and r != -1:
            ans = r
    print(ans)
