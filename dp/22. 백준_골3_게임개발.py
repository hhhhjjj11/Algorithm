# 정리
"""
위상정렬
1. 진입간선이 없는 루트노드들을 큐에 넣는다.
2. 큐에서 빼고 -> 해당 노드에 연결된 간선들을 전부 지운다.

dp[i] = i번 건물을 완성시키는데 걸리는 시각
"""
# 풀이
import sys
from collections import deque

N = int(input())
g = [[] for _ in range(N+1)] # g[i] = i의 진입간선(노드)
bt = [0]*(N+1)
for i in range(1,N+1):
    li = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(len(li)):
        if j == 0:
            bt[i] = li[j]
            continue
        if j == len(li)-1:
            break
        g[i].append(li[j])

topo = []
dp = [0]*(N+1)

Q = deque()
visited = [0]*(N+1)

while True:
    for i in range(1,N+1):
        if len(g[i]) == 0 and not visited[i]:
            Q.append(i)
            visited[i]=1

    if not Q:
        break

    while Q:
        node = Q.popleft()

        if dp[node] == 0:
            dp[node] = bt[node]

        topo.append(node)

        for i in range(1,N+1):
            if node in g[i]:
                g[i].remove(node)
                if dp[i] < dp[node] + bt[i] :
                    dp[i] = dp[node] + bt[i]

for i in range(1,N+1):
    print(dp[i])