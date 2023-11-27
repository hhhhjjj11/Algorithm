# 정리
"""
순환 역들을 다 구하고 활용하였음.

특벼한 아이디어는 없는듯. 걍 dfs bfs구현
"""
# 풀이
import sys
from collections import deque
sys.setrecursionlimit(10**4)
N = int(input())

g = {}

for _ in range(N):
    a,b = map(int,sys.stdin.readline().strip().split())
    if a in g:
        g[a].append(b)
    else:
        g[a] = [b]
    if b in g:
        g[b].append(a)
    else:
        g[b] = [a]

# print(g)

def isCycle(start, V, movecnt):
    for next_node in g[V]:
        # print(V,'의 nextnode : ', next_node)
        if movecnt > 1  and next_node == start:
            return True
        else:
            if not visited[next_node]:
                # print('탐색 이어감')
                visited[next_node] = 1
                res = isCycle(start, next_node, movecnt+1)
                if res:
                    return True
                visited[next_node] = 0
    return False

cycle = [0]*(N+1)
for node in g:
    # print('node',node)
    visited = [0]*(N+1)
    visited[node] =1
    if isCycle(node,node, 0):
        # print('순환이맞아요', node)
        cycle[node] = 1

res = [-1]
# print('cycle', cycle)

def countDistance_BFS(V):
    
    global CNT

    Q = deque([[V,0]])
    visited = [0]*(N+1)
    visited[V] = 1

    while Q:
        node_now, cnt = Q.popleft()
        for next_node in g[node_now]:
            if cycle[next_node]:
                CNT = cnt + 1
                break
            if not visited[next_node]:
                Q.append([next_node,cnt+1])
                visited[next_node] = 1

for node in range(1,N+1):
    if cycle[node]:
        res.append(0)
    else:
        CNT = 0
        countDistance_BFS(node)        
        res.append(CNT)

for i in range(1,N+1):
    print(res[i], end =" ")
