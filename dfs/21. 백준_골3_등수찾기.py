import sys

g_low = {}
g_high = {}

N, M, X = map(int,sys.stdin.readline().strip().split())

for _ in range(M):
    A,B = map(int, sys.stdin.readline().strip().split())
    
    if A in g_low:
        g_low[A].append(B)
    else:
        g_low[A] = [B]
    if B in g_high:
        g_high[B].append(A)
    else:
        g_high[B] = [A]

# print(g_low)
# print(g_high)

lowCnt = 0  # 자기보다 낮은 애들
highCnt = 0 # 자기보다 높은 애들

def dfs1(V):
    # print('1', V)
    global lowCnt
    if not V in g_low:
        return
    for node_next in g_low[V]:
        if not visited[node_next]:
            lowCnt += 1
            visited[node_next] = 1
            dfs1(node_next)

def dfs2(V):
    # print('2',V)
    global highCnt
    if not V in g_high:
        return
    for node_next in g_high[V]:
        if not visited[node_next]:
            highCnt += 1
            visited[node_next] = 1
            dfs2(node_next)

visited = [0]*(N+1)
dfs1(X)
visited = [0]*(N+1)
dfs2(X)

# print('lowcnt, highcnt', lowCnt,highCnt)
print(highCnt+1,N-lowCnt)
