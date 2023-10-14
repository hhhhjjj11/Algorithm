# 정리
"""
이거 걍 공식대로 풀어야함
안그러면 시간초과 해결 못함 V가
dfs bottom up으로 풀면 되긴하는데 시간초과뜸.

다음과 같은 명제를 이용한다.
"임의의 노드에서 가장 먼 노드는 트리의 지름을 이루는 두 노드 중 하나이다."

따라서 트리의 지름을 구하는 방법은
임의의 노드에서 가장 먼 노드를 구하고 (지름의 한 쪽 끝)

그 노드에서 다시 가장 먼 노드(지름의 나머지 한 쪽 끝)까지의 거리를 구하면 됨.

"""
# 풀이
import sys
sys.setrecursionlimit(10**5)
V = int(input())

g = [[] for _ in range(V+1)]

for _ in range(V):
    li = list(map(int,sys.stdin.readline().strip().split()))
    pa = li[0]
    for i in range(1,len(li)):
        if li[i] == -1:
            continue
        if i%2:
            g[pa].append([li[i], li[i+1]])

visited = [0]*(V+1)
record = [0]*(V+1)
visited[1] = 1

def dfs(X, sum):
    
    if record[X] < sum:
        record[X] = sum

    for node_next, l in g[X]:
        if visited[node_next] == 0:

            visited[node_next] = 1
            dfs(node_next, sum+l)
            visited[node_next] = 0

dfs(1, 0)
A = record.index(max(record))
visited = [0]*(V+1)
record = [0]*(V+1)
visited[A] = 1
dfs(A,0)

print(max(record))